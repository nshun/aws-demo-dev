# IAM ロールを使ったアクセス管理

## 概要

IAM ユーザー UserA (ポリシーなし)が S3 にアクセスするために、IAM ロール S3Support (AmazonS3ReadOnlyAccess)を引き受ける

## 手順

1. UserA の作成

```sh
# IAM ユーザーの作成
aws iam create-user --user-name UserA

# インラインポリシーの内容を確認 (${AccountID}は書き換える)
cat UserA-InlinePolicy.json

# UserA にインラインポリシーを付与
aws iam put-user-policy --user-name UserA --policy-name AssumeRolePolicy --policy-document file://UserA-InlinePolicy.json
```

2. S3Support の作成

```sh
# 信頼ポリシーの内容を確認 (${AccountID}は書き換える)
cat S3Support-TrustPolicy.json

# IAM ロールの作成
aws iam create-role --role-name S3Support --assume-role-policy-document file://S3Support-TrustPolicy.json

# 付与するポリシーの情報を確認
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# ポリシードキュメントを確認
aws iam get-policy-version --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess --version-id v2

# ポリシーを付与
aws iam attach-role-policy --role-name S3Support --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

3. 実際に操作してみる

```sh
# UserA にコンソールアクセスを許可
aws iam create-access-key --user-name UserA

# UserA に変更する(環境変数)
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=

# UserA に切り替わってるか確認
aws sts get-caller-identity

# 環境変数を削除
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY

#　UserA のプロファイルを作成
aws configure --profile UserA
code ~/.aws/credentials

# 実際に操作してみる (AccessDenied になる)
aws s3 ls --profile UserA

# S3Support を引き受けるための認証情報を払い出す
aws sts assume-role --profile UserA --role-session-name DevOnAWS --role-arn "arn:aws:iam::${AccountId}:role/S3Support"

# S3Support のプロファイルを作成
code ~/.aws/credentials

[S3Support]
aws_access_key_id =
aws_secret_access_key =
aws_session_token =

# プロファイルの確認
aws sts get-caller-identity --profile S3Support

# 右: 実際に操作してみる (成功)
aws s3 ls --profile S3Support
aws s3 ls --profile S3Support --recursive s3://${BucketName}
```

## 作成したリソースの削除

管理アカウントでログイン

```sh
# CLI プロファイルの削除
code ~/.aws/credentials

# アクセスキーの確認
aws iam list-access-keys --user-name UserA

# アクセスキーの削除
aws iam delete-access-key --user-name UserA --access-key $AccessKeyId

# UserA に付与してあるポリシーの確認
aws iam list-user-policies --user-name UserA

# インラインポリシーの削除
aws iam delete-user-policy --user-name UserA --policy-name AssumeRolePolicy

# User Aの削除
aws iam delete-user --user-name UserA

# S3Support に付与してあるポリシーの確認
aws iam list-attached-role-policies --role-name S3Support

# 付与してあるポリシーの解除
aws iam detach-role-policy --role-name S3Support --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# IAM ロールの削除
aws iam delete-role --role-name S3Support
```
