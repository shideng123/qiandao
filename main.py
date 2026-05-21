import requests
import os
import time

# 从 GitHub Secrets 读取
TOKEN = os.getenv("MINDVIDEO_TOKEN")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Referer": "https://www.mindvideo.ai/zh/image-to-image/"
}

# 签到接口（实测可用）
CHECKIN_URL = "https://www.mindvideo.ai/api/user/checkin"

def mindvideo_checkin():
    try:
        res = requests.post(CHECKIN_URL, headers=HEADERS, timeout=15)
        print(f"状态码: {res.status_code}")
        print(f"返回: {res.text}")

        if res.status_code in (200, 201):
            print("✅ MindVideo 签到成功")
        elif "already" in res.text or "重复" in res.text:
            print("✅ 今日已签到")
        else:
            print("❌ 签到失败，Token 可能过期")
    except Exception as e:
        print(f"❌ 异常: {e}")

if __name__ == "__main__":
    mindvideo_checkin()
