# SDK を使った S3 の CRUD 操作

## 概要

SDK(Python) を使ってバケット・オブジェクトの CRUD 操作を確認する

## 手順

1. バケットを作成してオブジェクト操作

- `python bucket.py`
  - s3:CreateBucket
  - s3:HeadBucket
- `python object.py`
  - s3:PutObject
  - s3:GetObject
  - s3:HeadObject
  - s3:DeleteObject

2. 一括操作

```sh
# SDK から一括操作
python batch.py

# CLI 高レベルコマンドで一括操作
aws s3 ls

BucketName=
aws s3 ls s3://${BucketName}

# 画像以外のオブジェクトを一括削除する
## 一旦 dryrun で対象を確認
aws s3 rm s3://${BucketName} --recursive --exclude '*.jpg' --dryrun

## 本番削除
aws s3 rm s3://${BucketName} --recursive --exclude '*.jpg'
```

## 作成したリソースの削除

1. `src/clean.py` を実行
