# API Gateway の定義に Swagger を使う

## 概要

- API Gateway の定義を Swagger 形式でエクスポート
- API Gateway 作成時に Swagger ファイルをインポートする

## 手順

1. MC から前に作った API の prod ステージにアクセス
2. エクスポートタブから swagger 形式でエクスポート
   - Swagger
   - JSON
   - API GW 拡張機能あり
3. API を削除
4. 新しく REST API を作成(インポート)
5. 実際に GET メソッドをテストして確認

## 作成したリソースの削除

1. MC から作成した API を削除
