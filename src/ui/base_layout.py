import streamlit as st



def style_background_home():
    st.markdown("""
        <style>
                .stApp {
                    background: #020008 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background: rgba(255,255,255,0.04) !important;
                    padding: 2.5rem !important;
                    border-radius: 1.5rem !important;
                    border: 1px solid rgba(139, 92, 246, 0.25) !important;
                    backdrop-filter: blur(20px) !important;
                    box-shadow: 0 0 40px rgba(139, 92, 246, 0.08), inset 0 1px 0 rgba(255,255,255,0.06) !important;
                    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
                }

                .stApp div[data-testid="stColumn"]:hover {
                    transform: translateY(-4px) !important;
                    box-shadow: 0 0 60px rgba(139, 92, 246, 0.18), inset 0 1px 0 rgba(255,255,255,0.1) !important;
                }
        </style>  
    """, unsafe_allow_html=True)
    

def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp {
                    background: #020008 !important;
                }
        </style>  
    """, unsafe_allow_html=True)
    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400&display=swap');

        /* ── Reset & Global ── */
        #MainMenu, footer, header { visibility: hidden; }

        .block-container {
            padding-top: 1.5rem !important;
        }

        /* ── Animated mesh background ── */
        .stApp::before {
            content: '';
            position: fixed;
            inset: 0;
            background:
                radial-gradient(ellipse 80% 50% at 20% 10%, rgba(88, 28, 235, 0.12) 0%, transparent 60%),
                radial-gradient(ellipse 60% 40% at 80% 80%, rgba(168, 85, 247, 0.08) 0%, transparent 60%),
                radial-gradient(ellipse 40% 60% at 50% 50%, rgba(59, 7, 100, 0.15) 0%, transparent 70%);
            pointer-events: none;
            z-index: 0;
        }

        /* Subtle grid overlay */
        .stApp::after {
            content: '';
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(139, 92, 246, 0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(139, 92, 246, 0.04) 1px, transparent 1px);
            background-size: 60px 60px;
            pointer-events: none;
            z-index: 0;
        }

        /* ── Typography ── */
        h1 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 800 !important;
            font-size: 3.8rem !important;
            line-height: 1.05 !important;
            letter-spacing: -0.02em !important;
            background: linear-gradient(135deg, #ffffff 0%, #c4b5fd 50%, #8b5cf6 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            margin-bottom: 0.25rem !important;
        }

        h2 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 700 !important;
            font-size: 2rem !important;
            line-height: 1.1 !important;
            background: linear-gradient(135deg, #ffffff 0%, #c4b5fd 70%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            margin-bottom: 0rem !important;
        }

        h3 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 600 !important;
            color: #e2e8f0 !important;
        }

        h4, p {
            font-family: 'DM Sans', sans-serif !important;
            color: #94a3b8 !important;
        }

        /* ── All text defaults ── */
        .stApp, .stMarkdown, label, .stSelectbox, .stTextInput {
            font-family: 'DM Sans', sans-serif !important;
            color: #cbd5e1 !important;
        }

        /* ── Buttons ── */
        button[kind="primary"] {
            font-family: 'Syne', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.875rem !important;
            letter-spacing: 0.01em !important;
            border-radius: 0.75rem !important;
            background: linear-gradient(135deg, #7c3aed 0%, #8b5cf6 50%, #a78bfa 100%) !important;
            color: white !important;
            border: none !important;
            padding: 0.65rem 1.5rem !important;
            box-shadow: 0 0 20px rgba(139, 92, 246, 0.4), inset 0 1px 0 rgba(255,255,255,0.15) !important;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
            position: relative !important;
        }

        button[kind="primary"]:hover {
            transform: translateY(-2px) scale(1.02) !important;
            box-shadow: 0 0 35px rgba(139, 92, 246, 0.6), 0 8px 25px rgba(124, 58, 237, 0.4) !important;
        }

        button[kind="secondary"] {
            font-family: 'Syne', sans-serif !important;
            font-weight: 500 !important;
            font-size: 0.875rem !important;
            border-radius: 0.75rem !important;
            background: rgba(255,255,255,0.05) !important;
            color: #a78bfa !important;
            border: 1px solid rgba(139, 92, 246, 0.3) !important;
            padding: 0.65rem 1.5rem !important;
            transition: all 0.25s ease !important;
        }

        button[kind="secondary"]:hover {
            background: rgba(139, 92, 246, 0.12) !important;
            border-color: rgba(139, 92, 246, 0.6) !important;
            transform: translateY(-1px) !important;
        }

        button[kind="tertiary"] {
            font-family: 'Syne', sans-serif !important;
            font-weight: 500 !important;
            font-size: 0.875rem !important;
            border-radius: 0.75rem !important;
            background: rgba(255, 255, 255, 0.03) !important;
            color: #64748b !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            padding: 0.65rem 1.5rem !important;
            transition: all 0.2s ease !important;
        }

        button[kind="tertiary"]:hover {
            background: rgba(255, 255, 255, 0.07) !important;
            color: #94a3b8 !important;
            transform: translateY(-1px) !important;
        }

        /* ── Input fields ── */
        .stTextInput > div > div > input,
        .stSelectbox > div > div {
            font-family: 'DM Sans', sans-serif !important;
            background: rgba(255,255,255,0.04) !important;
            border: 1px solid rgba(139, 92, 246, 0.2) !important;
            border-radius: 0.75rem !important;
            color: #e2e8f0 !important;
            padding: 0.65rem 1rem !important;
            transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
        }

        .stTextInput > div > div > input:focus {
            border-color: rgba(139, 92, 246, 0.6) !important;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.12) !important;
            outline: none !important;
        }

        .stTextInput > div > div > input::placeholder {
            color: #475569 !important;
        }

        /* ── Dividers ── */
        hr {
            border: none !important;
            border-top: 1px solid rgba(139, 92, 246, 0.15) !important;
            margin: 1.5rem 0 !important;
        }

        /* ── Spinner ── */
        .stSpinner > div {
            border-color: #7c3aed !important;
        }

        /* ── Dataframe ── */
        .stDataFrame {
            border: 1px solid rgba(139, 92, 246, 0.2) !important;
            border-radius: 1rem !important;
            overflow: hidden !important;
        }

        /* ── Toast ── */
        [data-testid="stToast"] {
            background: rgba(15, 5, 30, 0.95) !important;
            border: 1px solid rgba(139, 92, 246, 0.4) !important;
            border-radius: 0.75rem !important;
            backdrop-filter: blur(20px) !important;
            color: #e2e8f0 !important;
        }

        /* ── Dialog / modal ── */
        [data-testid="stDialog"] > div {
            background: #0d0620 !important;
            border: 1px solid rgba(139, 92, 246, 0.3) !important;
            border-radius: 1.25rem !important;
            backdrop-filter: blur(30px) !important;
            box-shadow: 0 25px 80px rgba(0,0,0,0.7), 0 0 60px rgba(139,92,246,0.1) !important;
        }

        /* ── Scrollbar ── */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(139, 92, 246, 0.3); border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(139, 92, 246, 0.5); }

        /* ── Containers ── */
        [data-testid="stContainer"] {
            border-radius: 1rem !important;
        }

        /* ── Info / Warning / Error alerts ── */
        [data-testid="stAlert"] {
            border-radius: 0.75rem !important;
            border: none !important;
        }

        /* ── Camera input ── */
        [data-testid="stCameraInput"] {
            border-radius: 1rem !important;
        }

        /* Code blocks */
        code {
            font-family: 'JetBrains Mono', monospace !important;
            background: rgba(139, 92, 246, 0.1) !important;
            border: 1px solid rgba(139, 92, 246, 0.2) !important;
            border-radius: 0.4rem !important;
            color: #c4b5fd !important;
            padding: 2px 6px !important;
        }

        </style>  
    """, unsafe_allow_html=True)