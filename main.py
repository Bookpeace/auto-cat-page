import os
import requests

# ข้อมูลที่เราเก็บใน GitHub Secrets
FB_PAGE_ID = os.environ.get("FB_PAGE_ID")
FB_ACCESS_TOKEN = os.environ.get("FB_ACCESS_TOKEN")
GOOGLE_FLOW_API_KEY = os.environ.get("GOOGLE_FLOW_API_KEY")

def get_video_from_flow():
    print("ส่งคำขอไปที่ Google Flow...")
    # นี่คือ URL สมมติที่ส่งคำสั่งไปให้ Flow เจนคลิป
    flow_url = "https://api.google-flow.com/v1/generate" 
    headers = {"Authorization": f"Bearer {GOOGLE_FLOW_API_KEY}"}
    data = {"prompt": "A cute fluffy kitten playing with yarn, 16 seconds, cinematic"}
    
    # ยิงคำสั่งไปขอคลิป
    response = requests.post(flow_url, headers=headers, json=data)
    
    # รับลิงก์วิดีโอที่ Flow เจนเสร็จแล้ว
    video_data = response.json()
    return video_data['video_url'], "น้องแมวขี้อ้อนมาแล้วจ้า! 🐾 #CuteCats"

def post_to_fb(video_url, caption):
    print("กำลังอัปโหลดขึ้น Facebook...")
    url = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/videos"
    payload = {
        'file_url': video_url,
        'description': caption,
        'access_token': FB_ACCESS_TOKEN
    }
    res = requests.post(url, data=payload)
    return res.text

# รันระบบ
url, text = get_video_from_flow()
result = post_to_fb(url, text)
print("ผลลัพธ์จาก Facebook:", result)
