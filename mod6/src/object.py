# 依存関係をインポート
import boto3

# 設定
region = 'ap-northeast-1'
filename = "cat.jpg"
key = "cat-cat.jpg"

# S3 クライアントの作成 (低レベル)
s3_client = boto3.client('s3', region_name=region)

# バケットの検索
bucket_name = [b["Name"] for b in s3_client.list_buckets()["Buckets"] if b["Name"].startswith('sample-bucket')][0]
print(f'対象バケット: {bucket_name}\n')

# S3 リソースの作成 (高レベル)
s3_resource = boto3.resource('s3', region_name=region)
bucket = s3_resource.Bucket(bucket_name)

# オブジェクトを作成
print('s3:PutObject')
res = bucket.upload_file(filename, key)
print(f'./{filename} -> s3://{bucket_name}/{key}\n')

# オブジェクトの情報取得
print('s3:HeadObject')
res = s3_client.head_object(Bucket=bucket_name, Key=key)
print(f'{res}\n')

# オブジェクトを読み込み
print('s3:GetObject')
bucket.download_file(key, key)
print(f's3://{bucket_name}/{key} -> ./{key}\n')

# 署名付きURLの発行
print('署名付きURLの発行 (60秒)')
res = s3_client.generate_presigned_url(
  'get_object',
  Params = {
    'Bucket': bucket_name,
    'Key': key
  },
  ExpiresIn=60
)
print(f'{res}\n')
