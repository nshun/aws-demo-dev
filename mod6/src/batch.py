# 依存関係をインポート
import boto3
import uuid

# 設定
region = 'ap-northeast-1'

# S3 クライアントの作成
s3_client = boto3.client('s3', region_name=region)
s3_resource = boto3.resource('s3', region_name=region)

# バケットの検索
bucket_name = [b["Name"] for b in s3_client.list_buckets()["Buckets"] if b["Name"].startswith('sample-bucket')][0]
print(f'対象バケット: {bucket_name}\n')

# S3 リソースの作成
bucket = s3_resource.Bucket(bucket_name)

# 一括処理
print('s3:PutObject 100回')
for i in range(100):
  key = str(uuid.uuid4())
  res = bucket.put_object(
    Key=key,
    Body=key
  )
