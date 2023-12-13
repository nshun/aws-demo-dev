# 依存関係をインポート
import uuid

import boto3

# 設定
region = "ap-northeast-1"

# S3 クライアントの作成
s3_client = boto3.client("s3", region_name=region)

# バケットの検索
bucket_name = [
    b["Name"]
    for b in s3_client.list_buckets()["Buckets"]
    if "Name" in b and b["Name"].startswith("sample-bucket")
][0]
print(f"対象バケット: {bucket_name}\n")

# 一括処理
print("s3:PutObject 100回")
for i in range(100):
    key = str(uuid.uuid4())
    res = s3_client.put_object(Bucket=bucket_name, Key=key, Body=key)
