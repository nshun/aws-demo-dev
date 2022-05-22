# IAM ロールを使ったアクセス管理

## 概要

IAM ユーザー UserA (ポリシーなし)が S3 にアクセスするために、IAM ロール S3Support (AmazonS3ReadOnlyAccess)を引き受ける

## 手順

1. UserA の作成

```sh
# IAM ユーザーの作成
aws iam create-user --user-name UserA

# インラインポリシーの内容を確認
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

# 付与するポリシーの中身を確認
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# ポリシーを付与
aws iam attach-role-policy --role-name S3Support --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

3. タブを水平分割
4. 実際に操作してみる

```sh
# 左: UserA にコンソールアクセスを許可
aws iam create-access-key --user-name UserA

# 右: UserA に変更する
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=

# 右: 切り替わってるか確認
aws sts get-caller-identity

# 左右: 実際に操作してみる (右は AccessDenied になる)
aws s3 ls

# 右: S3Support を引き受けるための認証情報を払い出す
aws sts assume-role --role-session-name DevOnAWS --role-arn "arn:aws:iam::${AccountId}:role/S3Support"

# 右: S3Support を引き受ける
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_SESSION_TOKEN=

# 右: 切り替わってるか確認
aws sts get-caller-identity

# 右: 実際に操作してみる (成功)
aws s3 ls
aws s3 ls --recursive s3://${BucketName}
```

## 作成したリソースの削除

```sh
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
