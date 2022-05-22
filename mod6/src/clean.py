# 依存関係をインポート
import boto3
import os

# 設定
region = 'ap-northeast-1'

# ダウンロードした画像の削除
d_path = 'cat-cat.jpg'
if os.path.exists(d_path):
  os.remove(d_path)

# S3 クライアントの作成
s3_client = boto3.client('s3', region_name=region)
s3_resource = boto3.resource('s3', region_name=region)

# バケットの検索
bucket_names = [b['Name'] for b in s3_client.list_buckets()['Buckets'] if b['Name'].startswith('sample-bucket')]

for bucket_name in bucket_names:
  print(f'対象バケット: {bucket_name}')
  bucket = s3_resource.Bucket(bucket_name)

  # すべてのオブジェクト削除
  bucket.objects.delete()

  # バケット削除
  bucket.delete()
  print('削除完了')
