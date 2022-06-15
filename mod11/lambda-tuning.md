# Lambda 関数のパフォーマンス最適化を行う

## 概要

- AWS Lambda Power Tuning tool を使用
  - https://github.com/alexcasalboni/aws-lambda-power-tuning/
- メモリ量と平均実行時間からパフォーマンス最適化とコスト最適化を行う
  - 設定メモリ量に比例して CPU パワーも増加
  - Lambda の料金は設定メモリ量と実行時間による

## 準備

1. AWS Lambda Power Tuning tool をデプロイ

```sh
sam deploy --template-file src/sam-lambda-power-tuning.yml --stack-name lambda-power-tuning-app --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
```

## 手順

1. MC から Step Functions にアクセス
2. powerTuningStateMachine を 2 つの関数で起動
   - listFunction (x86_64)
   - listFunction (arm64)

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

1. 実行結果の URL にアクセスし可視化

- [サンプル結果](<https://lambda-power-tuning.show/#gAAAAQACAAQABsAL;mO5HQgRWkkG2OjJBiM96QR+FL0Hj7J9B;XHzhM4ReqzNjd9gzl0+QNBTSlDQQeYQ1;gAAAAQACAAQABsAL;XchbQqDTSkHkXh1BagM/QTMzL0GcxDZB;K8rIM2rWPTNlB5IzEzwvNJrycDQesAA1;listFunction%20(x86_64);listFunction%20(arm64)>)

## 作成したリソースの削除

1. Power Tuning の削除

```sh
sam delete --stack-name lambda-power-tuning-app
```
