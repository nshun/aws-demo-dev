# DynamoDB をローカルでテストする

## 概要

- SAM

## 手順

1. アプリケーションコードを確認
   - `sam-app/hello_world/app.py`
2. Lambda のローカルテスト
   - 適当にブレークポイントを置く
   - ハンドラ関数上に出てくる `Edit: AWS...` をクリック
   - 右ペインでデバッグ設定をして Invoke
   - 実行結果を確認する
3. ビルド & デプロイ

```sh
sam build
sam deploy --stack-name demo-lambda --resolve-s3 --capabilities CAPABILITY_IAM
```

4. 呼び出し

```sh
# 同期呼び出し
aws lambda invoke --function-name demo-lambda \
  --payload '{"code":200}' --cli-binary-format raw-in-base64-out \
  out --log-type Tail --query 'LogResult' --output text | base64 -d

# 同期呼び出し(意図的なエラー)
aws lambda invoke --function-name demo-lambda \
  --payload '{"code":401}' --cli-binary-format raw-in-base64-out \
  out --log-type Tail --query 'LogResult' --output text | base64 -d

# 非同期呼び出し
aws lambda invoke --function-name demo-lambda --invocation-type Event request.json \
  --payload '{"code":202}' --cli-binary-format raw-in-base64-out

# 非同期呼び出し(意図的なエラー)
aws lambda invoke --function-name demo-lambda --invocation-type Event request.json \
  --payload '{"code":402}' --cli-binary-format raw-in-base64-out
```

5. MC で呼び出しログを確認
   - エラー時の再試行に注目

## 作成したリソースの削除

```sh
# アプリの削除
sam delete --stack-name demo-lambda
```
