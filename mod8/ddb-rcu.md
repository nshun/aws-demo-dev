# DynamoDB の一括操作をキャパシティを確認する

## 概要

- Scan と Query の違いを確認する

## 手順

1. DynamoDB ローカルを実行
   - `docker run -p 8000:8000 amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath .`
2. 高レベル API を使って 1000 件のデータを投入
   - `python ddb_batch_write.py`
3. ProductCategory が Book で、ID が 200 以下の件数を出力
   - Scan は全ての項目を取得したあとにフィルター
   - Query はプライマリキーの範囲で検索可能
   - 消費 RCU を比べる

```sh
# Scan
aws dynamodb scan --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --select COUNT \
    --filter-expression 'ProductCategory = :category and Id <= :id' \
    --expression-attribute-values file://expression-attributes.json \
    --return-consumed-capacity TOTAL

# Query
aws dynamodb query --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --select COUNT \
    --key-condition-expression "ProductCategory = :category and Id <= :id" \
    --expression-attribute-values file://expression-attributes.json \
    --return-consumed-capacity TOTAL
```

## 作成したリソースの削除

```sh
# テーブルの削除
aws dynamodb delete-table --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog
```
