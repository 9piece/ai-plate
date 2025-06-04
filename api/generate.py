import os
import json
from openai import OpenAI

client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=os.getenv("ARK_API_KEY")
)

MODEL_ID = os.getenv("MODEL_ID", "")

def handler(request):
    try:
        body = request.json()
        prompt = body.get("prompt", "")

        if not prompt or not MODEL_ID:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing prompt or MODEL_ID"})
            }

        # 发起图像生成请求
        response = client.images.generate(
            model=MODEL_ID,
            prompt=prompt,
            size="1024x1024",
            response_format="url",
            guidance_scale=3,
            watermark=True
        )

        image_url = response.data[0].url if response.data else ""

        return {
            "statusCode": 200,
            "body": json.dumps({"image_url": image_url})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
