import json


def lambda_handler(event, context):
    # 例外
    if "code" not in event:
        raise ValueError("code not found\n")
    if event["code"] >= 400:
        raise ValueError(f"error code: {event['code']}\n")

    return {
        "statusCode": event["code"],
        "body": json.dumps({
            "message": "hello world",
        })
    }
