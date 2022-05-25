# ライブラリのインポート
import os
import boto3
import uuid

# Cognito Identity Provider クライアントの作成
client = boto3.client('cognito-idp')

# 設定
client_id = os.environ['ClientId']
user_pool_id = os.environ['UserPoolId']
username = str(uuid.uuid4())
password = str(uuid.uuid4())

# ユーザー作成
response = client.admin_create_user(
    UserPoolId=user_pool_id,
    Username=username,
)

# パスワード設定
response = client.admin_set_user_password(
    UserPoolId=user_pool_id,
    Username=username,
    Password=password,
    Permanent=True
)

# レスポンスの表示
print(f'export Username={username}')
print(f'export Password={password}')
