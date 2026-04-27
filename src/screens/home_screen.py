import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    st.html("""
        <style>
        @keyframes pulse-dot { 0%,100%{opacity:1;transform:scale(1);} 50%{opacity:0.4;transform:scale(1.4);} }
        </style>
        <div style="text-align:center; margin-bottom:2.5rem;">
            <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(139,92,246,0.1); border:1px solid rgba(139,92,246,0.3); border-radius:999px; padding:6px 16px; margin-bottom:1rem;">
                <span style="width:7px; height:7px; border-radius:50%; background:#a78bfa; display:inline-block; box-shadow:0 0 8px #a78bfa; animation:pulse-dot 2s infinite;"></span>
                <span style="font-family:DM Sans,sans-serif; font-size:0.78rem; letter-spacing:0.12em; text-transform:uppercase; color:#a78bfa;">Powered by Computer Vision &amp; Voice AI</span>
            </div>
            <p style="font-family:DM Sans,sans-serif; color:rgba(148,163,184,0.8); font-size:1rem; max-width:420px; margin:0 auto; line-height:1.6;">Mark attendance in seconds with facial recognition and voice ID — no roll calls, no paper.</p>
        </div>
    """)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.html("""
            <div style="margin-bottom:0.75rem;">
                <div style="font-family:DM Sans,sans-serif; font-size:0.72rem; letter-spacing:0.18em; text-transform:uppercase; color:rgba(167,139,250,0.6); margin-bottom:0.4rem;">— For Students</div>
                <div style="font-family:Syne,sans-serif; font-weight:700; font-size:1.6rem; background:linear-gradient(135deg,#ffffff,#c4b5fd); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">I'm a Student</div>
                <p style="font-family:DM Sans,sans-serif; color:rgba(148,163,184,0.7); font-size:0.85rem; margin:0.5rem 0 0; line-height:1.5;">Log in with your face. Track your attendance. Zero effort.</p>
            </div>
        """)
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=105)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.html("""
            <div style="margin-bottom:0.75rem;">
                <div style="font-family:DM Sans,sans-serif; font-size:0.72rem; letter-spacing:0.18em; text-transform:uppercase; color:rgba(167,139,250,0.6); margin-bottom:0.4rem;">— For Educators</div>
                <div style="font-family:Syne,sans-serif; font-weight:700; font-size:1.6rem; background:linear-gradient(135deg,#ffffff,#c4b5fd); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">I'm a Teacher</div>
                <p style="font-family:DM Sans,sans-serif; color:rgba(148,163,184,0.7); font-size:0.85rem; margin:0.5rem 0 0; line-height:1.5;">Snap a photo. AI handles the rest. Instant records.</p>
            </div>
        """)
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=130)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    st.html("""
        <div style="margin-top:2.5rem; padding:1.25rem 1.5rem; background:rgba(139,92,246,0.05); border:1px solid rgba(139,92,246,0.12); border-radius:1rem; display:flex; justify-content:space-around; flex-wrap:wrap; gap:1rem;">
            <div style="text-align:center;">
                <div style="font-size:1.4rem; margin-bottom:2px;">📸</div>
                <div style="font-family:Syne,sans-serif; font-size:0.75rem; color:#c4b5fd; font-weight:600;">Face ID Login</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.4rem; margin-bottom:2px;">🎙️</div>
                <div style="font-family:Syne,sans-serif; font-size:0.75rem; color:#c4b5fd; font-weight:600;">Voice Recognition</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.4rem; margin-bottom:2px;">⚡</div>
                <div style="font-family:Syne,sans-serif; font-size:0.75rem; color:#c4b5fd; font-weight:600;">Instant Results</div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:1.4rem; margin-bottom:2px;">📊</div>
                <div style="font-family:Syne,sans-serif; font-size:0.75rem; color:#c4b5fd; font-weight:600;">Smart Analytics</div>
            </div>
        </div>
    """)

    footer_home()