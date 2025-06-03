import streamlit as st

def show_logo():
    """Display logo in the center if available."""
    try:
        col1, col2, col3 = st.columns([3, 2, 3])
        with col2:
            st.image("assets/logo.png")
    except Exception:
        pass

def render_chat_history(messages):
    for message in messages:
        if message["role"] == "assistant":
            st.markdown(f'<div class="assistant">{message["content"]}</div>', unsafe_allow_html=True)
        elif message["role"] == "user":
            st.markdown(f'<div class="user">{message["content"]}</div>', unsafe_allow_html=True)

def inject_chat_css():
    """Inject simple, classic chat CSS (original style)."""
    st.markdown(
        """
        <style>
            .assistant {
                padding: 10px;
                border-radius: 10px;
                max-width: 75%;
                background: none;
                text-align: left;
            }
            .user {
                padding: 10px;
                border-radius: 10px;
                max-width: 75%;
                background: none;
                text-align: right;
                margin-left: auto;
            }
            .assistant::before { content: "🤖 "; font-weight: bold; }
        </style>
        """,
        unsafe_allow_html=True
    )
