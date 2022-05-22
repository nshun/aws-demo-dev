package com.mycompany.app;

// 依存関係をインポート
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;

import java.util.UUID;

public class App {
    public static void main(String[] args) {
        // 設定
        String region = "ap-northeast-1";
        String bucket_name = "sample-bucket-" + UUID.randomUUID();
        System.out.println("作成するバケット名:" + bucket_name);

        //S3 クライアントの作成
        AmazonS3 s3Client = AmazonS3ClientBuilder.standard().withRegion(region).build();

        // バケットの作成
        s3Client.createBucket(bucket_name);

        // 明示的にクライアントをシャットダウン
        s3Client.shutdown();
    }
}
