import toml
import streamlit as st

def get_config_value(key, default=None):
    """Đọc giá trị từ config.toml theo key, trả về default nếu lỗi."""
    try:
        config = toml.load("../config.toml")
        return config.get(key, default)
    except Exception:
        return default

def get_welcome_message():
    """Lấy lời chào từ config.toml, rồi đến secrets, cuối cùng là mặc định."""
    msg = get_config_value("WELCOME_MESSAGE")
    if not msg:
        msg = st.secrets.get("WELCOME_MESSAGE")
    if not msg:
        msg = "Xin chào! Tôi là trợ lý AI của bạn."
    return msg

def get_secrets():
    """Lấy các biến BEARER_TOKEN và WEBHOOK_URL từ secrets."""
    BEARER_TOKEN = st.secrets.get("BEARER_TOKEN")
    WEBHOOK_URL = st.secrets.get("WEBHOOK_URL")
    if not BEARER_TOKEN or not WEBHOOK_URL:
        st.error("Thiếu BEARER_TOKEN hoặc WEBHOOK_URL trong secrets. Vui lòng kiểm tra lại file .streamlit/secrets.toml!")
        st.stop()
    return BEARER_TOKEN, WEBHOOK_URL
