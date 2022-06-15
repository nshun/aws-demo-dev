# Lambda 関数のパフォーマンス最適化を行う

## 概要

- AWS Lambda Power Tuning tool を使用して Lambda 関数のパフォーマンス最適化を行う
  - https://github.com/alexcasalboni/aws-lambda-power-tuning/

## 準備

1. AWS Lambda Power Tuning tool をデプロイ

```sh
sam deploy --template-file src/sam-lambda-power-tuning.yml --stack-name lambda-power-tuning-app --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
```

## 手順

1. MC から Step Functions にアクセス
2. powerTuningStateMachine を以下のペイロードで起動

```json
{
  "lambdaARN": "{ARN of list-function}",
  "num": 50,
  "payload": {
    "requestContext": {
      "authorizer": {
        "claims": {
          "cognito:username": "student"
        }
      }
    }
  }
}
```

3. 実行結果の URL にアクセスし可視化

## 作成したリソースの削除

1. Power Tuning の削除

```sh
sam delete --stack-name lambda-power-tuning-app
```
