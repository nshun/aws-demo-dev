# API Gateway のカナリアリリース

## 概要

- MC を使用して API Gateway をデプロイ
- カナリアリリースを有効にして挙動を確認

## 手順

1. MC で APIGW (REST API) を作成
   - 名前: `DemoAPI`
2. ルートに GET メソッドを追加
   - Mock 統合
   - 統合レスポンスのマッピングテンプレートを `{"v":1}` に変更
3. GET メソッドをテスト
4. API をデプロイ
   - ステージは `prod`
5. API を curl で叩いてみる
   - `curl {url}`
6. API のカナリアリリースを有効化
7. リソースから API を更新
   - 統合レスポンスのマッピングテンプレートを `{"v":2}` に変更
8. API を再デプロイ
   - ステージは `prod(Canary)`
9. API を curl で定期実行
   - `URL="{URL}"`
   - `while true;do curl $URL; sleep 2; done`
   - レスポンスの割合を確認
   - 実行をやめずに放置
10. Canary の割合を `50%` にする
11. Canary を昇格させる

## 作成したリソースの削除

1. 次の demo で使うので保持
