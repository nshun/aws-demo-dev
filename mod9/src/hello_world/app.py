import json
import log_layer


def lambda_handler(event, context):
    # log_layerの関数を使用してログ出力
    log_layer.print(event, context)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        })
    }
