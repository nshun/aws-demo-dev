# Cognito ユーザープールで認証を行う

## 概要

- Cognito ユーザープールでユーザー作成をする
- Cognito ユーザープールでパスワード認証し、レスポンスを確認する

## 準備

- Cognito のユーザープールを作成
- アプリクライアントを作成してパスワード認証を有効化

## 手順

1. コードの確認
   - `src/signup.py`
   - `src/signin.py`
2. ユーザー作成と認証を行う

```sh
# 環境変数を設定
export UserPoolId=
export ClientId=

# ユーザー作成
python src/signup.py

# 出力のコマンドでIDとPWを環境変数に設定する
export Username=
export Password=

# パスワードでサインイン
python src/signin.py
```

3. レスポンスを確認する
   - `response.json`
     - AccessToken, IdToken, RefreshToken
   - Base64 でエンコードされているので、デコードする
     - https://jwt.io/
   - Cognito のトークンは暗号化されていない
   - しかし、書き換えると署名の検証が失敗する

## 作成したリソースの削除

```sh
python src/clean.py
```

- Cognito ユーザープールの削除
