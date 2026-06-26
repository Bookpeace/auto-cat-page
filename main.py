import os
import requests

# ข้อมูลที่ดึงมาจาก GitHub Secrets
FB_PAGE_ID = os.environ.get("FB_PAGE_ID")
FB_ACCESS_TOKEN = os.environ.get("FB_ACCESS_TOKEN")
FLOW_API_KEY = os.environ.get("GOOGLE_FLOW_API_KEY")

def get_video_from_flow():
    # เปลี่ยน URL นี้เป็น Endpoint จริงของ Google Flow
    url = "https://api.google-flow.com/v1/generate" 
    headers = {"Authorization": f"Bearer {FLOW_API_KEY}"}
    payload = {"prompt": "cute cat"}
    
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    
    # ดึงค่า URL ของคลิปออกมา (ตรงนี้ต้องดูว่า Flow ส่งกลับมาในชื่อ key อะไร)
    return data['video_url']

def post_to_fb(video_url):
    url = f"https://graph.facebook.com/v19.0/{FB_PAGE_ID}/videos"
    payload = {
        'file_url': video_url,
        'description': "น้องแมวน่ารักฮีลใจ! 🐾",
        'access_token': FB_ACCESS_TOKEN
    }
    res = requests.post(url, data=payload)
    return res.text

if __name__ == "__main__":
    video_url = get_video_from_flow()
    print("ได้คลิปจาก Flow แล้ว กำลังโพสต์...")
    result = post_to_fb(video_url)
    print("ผลลัพธ์จาก Facebook:", result)
