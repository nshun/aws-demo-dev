# ライブラリのインポート
import os
import boto3

# Cognito Identity Provider クライアントの作成
client = boto3.client('cognito-idp')

# 設定
user_pool_id = os.environ['UserPoolId']
username = os.environ['Username']

# ユーザー削除
response = client.admin_delete_user(
    UserPoolId=user_pool_id,
    Username=username,
)
