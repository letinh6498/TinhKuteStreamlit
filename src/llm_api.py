import uuid
import requests
from config import get_secrets, get_config_value

BEARER_TOKEN, WEBHOOK_URL = get_secrets()

def create_session_id():
    """Generate a random session id."""
    return str(uuid.uuid4())

def get_llm_response(session_id, message):
    """Gửi câu hỏi tới LLM qua webhook, trả về phản hồi hoặc thông báo tiếng Việt nếu lỗi."""
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "sessionId": session_id,
        "chatInput": message
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        response_data = response.json()
        if isinstance(response_data, list) and response_data and "output" in response_data[0]:
            return response_data[0]["output"]
        elif isinstance(response_data, dict) and "output" in response_data:
            return response_data["output"]
        else:
            return "Xin lỗi, hệ thống AI không trả về kết quả hợp lệ. Vui lòng thử lại sau!"
    except requests.exceptions.Timeout:
        return "Xin lỗi, hệ thống AI đang bận hoặc phản hồi chậm. Vui lòng thử lại sau vài phút!"
    except requests.exceptions.RequestException:
        return "Xin lỗi, không thể kết nối tới hệ thống AI. Vui lòng kiểm tra lại kết nối hoặc thử lại sau!"
