# CDK を使った開発

## 概要

- CDK 環境を初期化する
- CDK アプリケーションを構築・テスト・デプロイ

## 手順

1. CDK アプリの初期化

```sh
# ディレクトリの準備
cd mod13
mkdir cdk-app
cd cdk-app

# CDK アプリケーションの構築
cdk init --language=typescript
```

2. cdk_app/lib/cdk-app-stack.ts を編集

```ts
new s3.Bucket(this, 'DemoBucket', { removalPolicy: RemovalPolicy.DESTROY });
```

3. CDK のデプロイ

```sh
# cloudformation テンプレートの作成
cdk synth

# デプロイ
cdk deploy
```

4. 作成された S3 バケットを確認 (demobucket)

```sh
aws s3 ls
```

## 作成したリソースの削除

```sh
# CDK が作成した CloudFormation スタックの削除
cdk destroy

# cdk アプリの削除
rm -rf cdk-app
```
