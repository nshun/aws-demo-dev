# DynamoDB の一括操作をキャパシティを確認する

## 概要

- 項目の CRUD 操作を確認
  - PutItem, GetItem, UpdateItem, DeleteItem

## 手順

1. DynamoDB ローカルを実行
   - `docker run -p 8000:8000 amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath .`
2. アイテムに対して CRUD 操作を行う

```sh
# PutItem
aws dynamodb put-item --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --item '{"ProductCategory": {"S": "Computer"}, "Id": {"N": "10000"}}'

# GetItem
aws dynamodb get-item --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --key '{"ProductCategory": {"S": "Computer"}, "Id": {"N": "10000"}}'

# PutItem
aws dynamodb put-item --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --item '{"ProductCategory": {"S": "Computer"}, "Id": {"N": "10000"}, "Title": {"S": "Computer-1-1000"}, "Price": {"N": "1000"}}'

# GetItem (上書きされたことを確認)
aws dynamodb get-item --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --key '{"ProductCategory": {"S": "Computer"}, "Id": {"N": "10000"}}'

# UpdateItem
aws dynamodb update-item --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --key '{"ProductCategory": {"S": "Computer"}, "Id": {"N": "10000"}}' \
    --update-expression 'SET Price = Price - :p' \
    --expression-attribute-values '{":p": {"N": "400"}}' \
    --return-values ALL_NEW

# 条件付き UpdateItem x 2
aws dynamodb update-item --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --key '{"ProductCategory": {"S": "Computer"}, "Id": {"N": "10000"}}' \
    --update-expression 'SET Price = Price - :p' \
    --expression-attribute-values '{":p": {"N": "400"}}' \
    --condition-expression "Price > :p" \
    --expression-attribute-values '{":p": {"N": "400"}}' \
    --return-values ALL_NEW

# DeleteItem
aws dynamodb delete-item  --endpoint-url http://localhost:8000 \
    --table-name ProductCatalog \
    --key '{"ProductCategory": {"S": "Computer"}, "Id": {"N": "10000"}}' \
    --return-values ALL_OLD
```

## 作成したリソースの削除

- ddb-item-crud でも使うので維持
