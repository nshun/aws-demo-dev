# DynamoDB をローカルでテストする

## 概要

- Docker を使って DynamoDB をローカルでデプロイ
- AWS CLI で DunamoDB ローカルを操作
- NoSQL Workbench で GUI 操作

## 手順

1. DynamoDB ローカルを実行
   - `docker run -p 8000:8000 amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath .`
2. 別タブで DynamoDB 操作
   - dynamodb api にアクセスできることを確認
   - 読み取り整合性で消費キャパシティが違うことを確認

```sh
# テーブル一覧
aws dynamodb list-tables --endpoint-url http://localhost:8000

# テーブル作成 (プライマリキー＝ProductCategory + Id)
aws dynamodb create-table --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --attribute-definitions \
        AttributeName=ProductCategory,AttributeType=S \
        AttributeName=Id,AttributeType=N \
    --key-schema AttributeName=ProductCategory,KeyType=HASH AttributeName=Id,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD

# 項目の追加
aws dynamodb batch-write-item --endpoint-url http://localhost:8000 \
    --request-items file://ProductCatalog.json \
    --return-consumed-capacity TOTAL

# GetItem (結果整合性)
aws dynamodb get-item --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --projection-expression "Title,Price" \
    --key file://key.json \
    --return-consumed-capacity TOTAL

# GetItem (強い整合性)
aws dynamodb get-item --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --consistent-read \
    --projection-expression "Title,Price" \
    --key file://key.json \
    --return-consumed-capacity TOTAL
```

3. NoSQL WorkBench で接続して確認
   - [NoSQL Workbench](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/workbench.html) をインストール
   - 操作を試して、コード出力まで確認
     - Query, Scan
   - PartiQL を実行
     - `SELECT * FROM ProductCatalog`

```sh
aws dynamodb execute-statement --endpoint-url http://localhost:8000 \
    --statement "SELECT * FROM ProductCatalog"
``

## 作成したリソースの削除

- Mod 8 でも使うので維持
```
