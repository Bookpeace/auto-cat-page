import os
import requests

# ดึงรหัสลับจาก GitHub มาใช้งาน
FB_PAGE_ID = os.environ.get("FB_PAGE_ID")
FB_ACCESS_TOKEN = os.environ.get("FB_ACCESS_TOKEN")

print("กำลังเริ่มทำงาน...")

# ตรงนี้เดี๋ยวเราค่อยมาใส่ API ของ Google Flow ทีหลัง
video_url = "https://example.com/mock_video.mp4" 
caption = "ทดสอบบอทแมวอัตโนมัติ 🐾"

print("กำลังส่งขึ้น Facebook...")
url = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/videos"
payload = {
    'file_url': video_url,
    'description': caption,
    'access_token': FB_ACCESS_TOKEN
}

# สั่งยิงข้อมูล
response = requests.post(url, data=payload)
print("ผลลัพธ์:", response.text)
