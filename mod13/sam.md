# SAM を使った開発

## 概要

- SAM 環境を初期化する
- Application Composer による可視化 & 構築
- SAM アプリケーションを構築・テスト・デプロイ

## 手順

```sh
cd mod13

# テンプレートを使った SAM アプリケーションの構築
## 1 - AWS Quick Start Templates
## 1 - Hello World Example
## Use the most popular runtime and package type? (Python and zip) [y/N]: y
## その他は ENTER 押すだけ
sam init

# Application Composer による可視化 & 構築

# ビルド
cd sam-app
sam build

# ローカルテスト(Lamda)
sam local invoke HelloWorldFunction --event events/event.json

# ローカルテスト(API)
sam local start-api
curl http://localhost:3000/hello

# デプロイ
sam deploy --guided
```

## 作成したリソースの削除

```sh
# SAM が作成した CloudFormation スタックの削除
sam delete --stack-name sam-app

# sam アプリの削除
rm -rf sam-app
```
