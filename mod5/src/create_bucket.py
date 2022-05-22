# 依存関係をインポート
import boto3
import uuid

# 設定
region = 'ap-northeast-1'
bucket_name = f'sample-bucket-{uuid.uuid4()}'
print(f'作成するバケット名: {bucket_name}')

# S3 クライアントの作成
s3_client = boto3.client('s3', region_name=region)

# バケットの作成
s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)
