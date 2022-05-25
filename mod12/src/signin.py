# ライブラリのインポート
import os
import json
import boto3

# Cognito Identity Provider クライアントの作成
client = boto3.client('cognito-idp')

# 設定
client_id = os.environ['ClientId']
user_pool_id = os.environ['UserPoolId']
username = os.environ['Username']
password = os.environ['Password']

# ユーザー認証 (ユーザー名 + パスワード)
response = client.initiate_auth(
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': username,
        'PASSWORD': password
    },
    ClientId=client_id,
)

# レスポンスの保存
with open('response.json', 'w') as f:
    json.dump(response, f, indent=2, ensure_ascii=False)
