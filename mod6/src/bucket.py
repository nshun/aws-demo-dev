# 依存関係をインポート
import uuid

import boto3
import botocore.exceptions

# 設定
region = "ap-northeast-1"
bucket_name = f"sample-bucket-{uuid.uuid4()}"
print(f"作成するバケット名: {bucket_name}")

# S3 クライアントの作成
s3_client = boto3.client("s3", region_name=region)

# バケット名の重複チェック
try:
    s3_client.head_bucket(Bucket=bucket_name)
    raise SystemExit("その名前のバケットはアカウント内に既に存在しています")
except botocore.exceptions.ClientError as e:
    if "Error" in e.response and "Code" in e.response["Error"]:
        error_code = int(e.response["Error"]["Code"])
        if error_code == 404:
            print("その名前のバケットは AWS には存在しません")
        if error_code == 403:
            raise SystemExit("その名前のバケットは別の AWS アカウントに存在します")

# バケットの作成
s3_client.create_bucket(
    Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
)
print("バケット作成をリクエストしました")

# バケットが作成されるのを待つ
waiter = s3_client.get_waiter("bucket_exists")
waiter.wait(Bucket=bucket_name)
print("バケット作成が完了しました")

# バケットの情報を取得
print("s3:HeadBucket")
res = s3_client.head_bucket(Bucket=bucket_name)
print(f"{res}\n")
