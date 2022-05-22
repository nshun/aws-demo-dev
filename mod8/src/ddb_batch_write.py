# 依存関係をインポート
import boto3
import random

# 設定
categories = ["Book", "Bicycle", "CD", "Food"]

# DynamoDB リソースの作成
ddb_resource = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = ddb_resource.Table('ProductCatalog')

# サンプルデータ生成用の関数
def createSample(i):
  category = random.choice(categories)
  id = i + 1
  price = random.randint(1, 70) * 10

  sample = {
    "Id": id,
    "Price": price,
    "Title": f"{category}-{id}-{price}",
    "ProductCategory": category
  }
  return sample

# 一括データ挿入
with table.batch_writer() as batch:
  for i in range(1000):
    item = createSample(i)
    batch.put_item(
        Item=item
    )
