import json


def lambda_handler(event, context):
    # イベントの中身を出力
    print(f"event={event}")

    # 例外
    if "code" not in event or event["code"] >= 400:
        raise ValueError(f"error code: {event['code']}")

    return {
        "statusCode": event["code"],
        "body": json.dumps({
            "message": "hello world",
        })
    }
