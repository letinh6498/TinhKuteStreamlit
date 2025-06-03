from ui import show_logo, render_chat_history, inject_chat_css
from config import get_welcome_message
from llm_api import create_session_id, get_llm_response
import streamlit as st

# --- Main app ---
def main():
    inject_chat_css()
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = create_session_id()
    # Luôn hiển thị logo và welcome message khi chưa chat
    show_logo()
    st.markdown(
        f"""<h1 style='text-align: center; font-size: 24px;'>{get_welcome_message()}</h1>""",
        unsafe_allow_html=True
    )
    render_chat_history(st.session_state.messages)
    prompt = st.chat_input("Nhập nội dung cần trao đổi ở đây nhé?")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f'<div class="user">{prompt}</div>', unsafe_allow_html=True)
        with st.spinner("Đang chờ phản hồi từ AI..."):
            llm_response = get_llm_response(st.session_state.session_id, prompt)
        st.markdown(f'<div class="assistant">{llm_response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": llm_response})

if __name__ == "__main__":
    main()