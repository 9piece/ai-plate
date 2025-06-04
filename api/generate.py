import json
import os
import requests

API_URL = "https://ark.cn-beijing.volces.com/api/v3/drive/prediction"
MODEL_ID = "ep-20250603194600-lxnmn"

def handler(request):
    try:
        body = request.json()
        prompt = body.get("prompt", "")

        ACCESS_KEY = os.getenv("ACCESS_KEY")
        SECRET_KEY = os.getenv("SECRET_KEY")

        if not ACCESS_KEY or not SECRET_KEY:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Missing ACCESS_KEY or SECRET_KEY in environment variables."})
            }

        payload = {
            "model_id": MODEL_ID,
            "input": {"prompt": prompt}
        }

        headers = {
            "Authorization": f"Bearer {ACCESS_KEY}:{SECRET_KEY}",
            "Content-Type": "application/json"
        }

        res = requests.post(API_URL, json=payload, headers=headers)
        result = res.json()
        image_url = result.get("data", {}).get("prediction_result", {}).get("image_url", "")

        return {
            "statusCode": 200,
            "body": json.dumps({"image_url": image_url})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }