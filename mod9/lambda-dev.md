# Lambda のナイーブな開発

## 概要

- ツールを使わずに愚直に Lambda 関数をデプロイする

## 手順

1. Lambda 関数を確認する

   - `src/hello_world` : メイン関数
   - `src/log_layer` : ログ出力用のレイヤー

2. Lambda レイヤーのデプロイ

```sh
# デプロイディレクトリの作成 (これが zip にされる)
cd src/log_layer
mkdir python

# ライブラリのインストール
pip install --target ./python -r requirements.txt

# デプロイディレクトリにコードを追加
cp *.py ./python

# デプロイパッケージを作成 (zip)
zip -r layer.zip python

# .zip ファイルをレイヤーとしてデプロイ
aws lambda publish-layer-version \
  --layer-name log-layer \
  --zip-file fileb://layer.zip \
  --compatible-runtimes python3.11
```

3. メインの Lambda 関数をデプロイ

```sh
# 信頼ポリシーを確認
cd ../..
cat src/LambdaTrustPolicy.json

# 実行ロールを作成
aws iam create-role --role-name lambda-ex --assume-role-policy-document file://src/LambdaTrustPolicy.json

# デプロイパッケージ (zip) を作成
cd src/hello_world
zip package.zip app.py

# Lambda 関数の作成 ({RoleArn} を書き換え)
aws lambda create-function --function-name demo-python \
  --zip-file fileb://package.zip --handler app.lambda_handler --runtime python3.11 \
  --role {RoleArn}

# Lambda 関数にレイヤーを追加 ({LayerVersionArn} を書き換え)
aws lambda update-function-configuration \
  --function-name demo-python \
  --layers {LayerVersionArn}
```

4. マネジメントコンソールで `demo-python` を確認

5. 関数のテスト
   - 実行権限 -> 実行ロールのポリシー
   - 課金時間(Billed Duration) -> タイムアウト設定
   - 消費メモリ(Max Memory Used) -> メモリ設定
   - イベント、コンテキストの中身

```sh
# Lambda 関数の実行
aws lambda invoke --function-name demo-python \
  out --log-type Tail --query 'LogResult' --output text | base64 -d

# Lambda 関数の実行 (payload あり)
aws lambda invoke --function-name demo-python \
  --payload '{"key":"value"}' --cli-binary-format raw-in-base64-out \
  out --log-type Tail --query 'LogResult' --output text | base64 -d
```

6. 関数のバージョン発行・エイリアス作成

## 作成したリソースの削除

```sh
# Lambda 関数の削除
aws lambda delete-function --function-name demo-python

# Lambda レイヤーの削除
aws lambda delete-layer-version --layer-name log-layer --version-number 1

# 実行ロールの削除
aws iam delete-role --role-name lambda-ex

# ビルドファイルの削除
cd src
rm -r */out
rm -r */*.zip
rm -r log_layer/python
```
