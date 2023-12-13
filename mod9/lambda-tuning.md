# Lambda 関数のパフォーマンス最適化を行う

## 概要

- AWS Lambda Power Tuning tool を使用
  - https://github.com/alexcasalboni/aws-lambda-power-tuning/
- メモリ量と平均実行時間からパフォーマンス最適化とコスト最適化を行う
  - 設定メモリ量に比例して CPU パワーも増加
  - Lambda の料金は設定メモリ量と実行時間による

## 準備

AWS Lambda Power Tuning tool をデプロイ
https://github.com/alexcasalboni/aws-lambda-power-tuning/blob/master/README-DEPLOY.md

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

- [サンプル結果](<https://lambda-power-tuning.show/#gAAAAQACAAQABsAL;ZmYgQt7dfUEiIiJBZmYOQQAAGEEAACBB;+uW4M5dPkDNwbcYzilkiNJ5KhzQQeQQ1;gAAAAQACAAQABsAL;7+48Qs3MTEF3dxdBiYgYQby7I0GrqhpB;EzyvM2rWPTNlB5IzZQcSNJrycDTdetY0;listFunction(x86_64);listFunction(arm64)>)

## 作成したリソースの削除

Lambda コンソールのアプリケーションページで `serverlessrepo-aws-lambda-power-tuning` を削除
