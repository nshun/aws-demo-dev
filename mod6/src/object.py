# 依存関係をインポート
import boto3

# 設定
region = "ap-northeast-1"
filename = "cat.jpg"
key = "cat-cat.jpg"

# S3 クライアントの作成 (低レベル)
s3_client = boto3.client("s3", region_name=region)

# バケットの検索
bucket_name = [
    b["Name"]
    for b in s3_client.list_buckets()["Buckets"]
    if "Name" in b and b["Name"].startswith("sample-bucket")
][0]
print(f"対象バケット: {bucket_name}\n")

# オブジェクトを作成
print("s3:PutObject")
res = s3_client.upload_file(filename, bucket_name, key)
print(f"uploaded: ./{filename} -> s3://{bucket_name}/{key}\n")

# オブジェクトの情報取得
print("s3:HeadObject")
res = s3_client.head_object(Bucket=bucket_name, Key=key)
print(f"{res}\n")

# オブジェクトを読み込み
print("s3:GetObject")
s3_client.download_file(bucket_name, key, key)
print(f"downloaded: s3://{bucket_name}/{key} -> ./{key}\n")

# 署名付きURLの発行
print("署名付きURLの発行 (120秒)")
res = s3_client.generate_presigned_url(
    "get_object", Params={"Bucket": bucket_name, "Key": key}, ExpiresIn=120
)
print(f"{res}\n")
