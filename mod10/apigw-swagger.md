# API Gateway の定義に Swagger を使う

## 概要

- API Gateway の定義を Swagger 形式でエクスポート
- API Gateway 作成時に Swagger ファイルをインポートする

## 手順

### Swagger UI を使った API テスト

1. MC から前に作った API の prod ステージにアクセス
2. エクスポートタブから swagger 形式でエクスポート
   - Swagger
   - JSON
   - API GW 拡張機能あり
3. 以下 `FILE_NAME` をファイル名に置換して実行

```sh
docker run -p 80:8080 -e SWAGGER_JSON=/local/FILE_NAME -v ~/Downloads:/local swaggerapi/swagger-ui
```

4. http://localhost:80/ にアクセスして API テスト

### Swagger 定義ファイルからインポート

1. 新しく REST API を作成(インポート)
2. 実際に GET メソッドをテストして確認

## 作成したリソースの削除

1. MC から作成した API を削除 × 2
