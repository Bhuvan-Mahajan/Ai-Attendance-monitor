import streamlit as st


def header_home():
    st.html("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&family=DM+Sans:wght@300;400&display=swap');

        @keyframes orbit {
            from { transform: rotate(0deg); }
            to   { transform: rotate(360deg); }
        }
        @keyframes orbit-reverse {
            from { transform: rotate(0deg); }
            to   { transform: rotate(-360deg); }
        }
        @keyframes pulse-glow {
            0%, 100% { opacity: 0.5; transform: scale(1); }
            50%       { opacity: 1;   transform: scale(1.18); }
        }
        @keyframes dot-pulse {
            0%, 100% { box-shadow: 0 0 6px 2px #f472b6; transform: scale(1); }
            50%       { box-shadow: 0 0 18px 6px #f472b6; transform: scale(1.4); }
        }
        @keyframes shimmer {
            0%   { background-position: -400% center; }
            100% { background-position:  400% center; }
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50%       { transform: translateY(-8px); }
        }
        @keyframes fade-in-up {
            from { opacity: 0; transform: translateY(16px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        @keyframes spin-dash {
            from { stroke-dashoffset: 0; }
            to   { stroke-dashoffset: -220; }
        }

        .sc-logo-wrap {
            position: relative;
            width: 140px;
            height: 140px;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: float 4s ease-in-out infinite;
        }

        .sc-glow-ring {
            position: absolute;
            inset: -20px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(244,114,182,0.28) 0%, rgba(124,58,237,0.18) 45%, transparent 70%);
            animation: pulse-glow 3s ease-in-out infinite;
        }

        .sc-orbit-svg {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            animation: orbit 5s linear infinite;
        }

        .sc-orbit-svg-rev {
            position: absolute;
            inset: -18px;
            width: calc(100% + 36px);
            height: calc(100% + 36px);
            animation: orbit-reverse 8s linear infinite;
        }

        .sc-logo-core {
            position: relative;
            z-index: 2;
            width: 100px;
            height: 100px;
            filter: drop-shadow(0 0 22px rgba(244,114,182,0.55));
        }

        .sc-wordmark {
            margin-top: 1.4rem;
            text-align: center;
            animation: fade-in-up 0.8s ease both;
            animation-delay: 0.2s;
        }

        .sc-wordmark-text {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 3.6rem;
            line-height: 1;
            letter-spacing: -0.04em;
            background: linear-gradient(90deg,
                #ffffff 0%,
                #f9a8d4 20%,
                #c4b5fd 40%,
                #ffffff 55%,
                #f9a8d4 70%,
                #7c3aed 85%,
                #ffffff 100%
            );
            background-size: 300% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 4s linear infinite;
        }

        .sc-tagline {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.75rem;
            letter-spacing: 0.28em;
            text-transform: uppercase;
            color: rgba(249,168,212,0.6);
            margin-top: 0.5rem;
            animation: fade-in-up 0.8s ease both;
            animation-delay: 0.5s;
        }

        .sc-header-root {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-bottom: 2.5rem;
            margin-top: 2rem;
        }
        </style>

        <div class="sc-header-root">
            <div class="sc-logo-wrap">
                <div class="sc-glow-ring"></div>

                <svg class="sc-orbit-svg" viewBox="0 0 140 140" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="orb-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stop-color="#f472b6" stop-opacity="0"/>
                            <stop offset="50%" stop-color="#f472b6" stop-opacity="1"/>
                            <stop offset="100%" stop-color="#7c3aed" stop-opacity="0"/>
                        </linearGradient>
                    </defs>
                    <circle cx="70" cy="70" r="62" fill="none" stroke="url(#orb-grad)" stroke-width="1.5" stroke-dasharray="60 330"/>
                    <circle cx="70" cy="8" r="5" fill="#f472b6" style="filter:drop-shadow(0 0 4px #f472b6);"/>
                </svg>

                <svg class="sc-orbit-svg-rev" viewBox="0 0 176 176" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="orb-grad2" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stop-color="#7c3aed" stop-opacity="0"/>
                            <stop offset="50%" stop-color="#a78bfa" stop-opacity="0.7"/>
                            <stop offset="100%" stop-color="#7c3aed" stop-opacity="0"/>
                        </linearGradient>
                    </defs>
                    <circle cx="88" cy="88" r="80" fill="none" stroke="url(#orb-grad2)" stroke-width="1" stroke-dasharray="30 470"/>
                    <circle cx="88" cy="8" r="3.5" fill="#a78bfa" style="filter:drop-shadow(0 0 3px #a78bfa);"/>
                </svg>

                <svg class="sc-logo-core" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="core-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#f472b6"/>
                            <stop offset="100%" stop-color="#7c3aed"/>
                        </linearGradient>
                        <linearGradient id="s-grad" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" stop-color="#f9a8d4"/>
                            <stop offset="100%" stop-color="#a78bfa"/>
                        </linearGradient>
                    </defs>
                    <rect x="0" y="0" width="160" height="160" rx="38" fill="#0a0015"/>
                    <rect x="2" y="2" width="156" height="156" rx="36" fill="none" stroke="url(#core-grad)" stroke-width="1.2" opacity="0.5"/>
                    <path d="M100 48 Q100 34 80 34 Q60 34 60 52 Q60 70 80 70 Q100 70 100 88 Q100 106 80 106 Q60 106 60 94"
                          stroke="url(#s-grad)" stroke-width="7" fill="none" stroke-linecap="round"/>
                    <circle cx="104" cy="36" r="5.5" fill="#7c3aed" opacity="0.95"/>
                    <circle cx="56" cy="96" r="4" fill="#f472b6" opacity="0.8"/>
                </svg>
            </div>

            <div class="sc-wordmark">
                <div class="sc-wordmark-text">PREZENCE</div>
                <div class="sc-tagline">AI-Powered Attendance</div>
            </div>
        </div>
    """)


def header_dashboard():
    st.html("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&display=swap');

        @keyframes orbit-sm {
            from { transform: rotate(0deg); }
            to   { transform: rotate(360deg); }
        }
        @keyframes float-sm {
            0%, 100% { transform: translateY(0px); }
            50%       { transform: translateY(-3px); }
        }

        .sc-dash-wrap {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 0.25rem 0;
        }

        .sc-dash-logo {
            position: relative;
            width: 58px;
            height: 58px;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: float-sm 3.5s ease-in-out infinite;
        }

        .sc-dash-orbit {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            animation: orbit-sm 4s linear infinite;
        }

        .sc-dash-core {
            position: relative;
            z-index: 2;
            width: 44px;
            height: 44px;
            filter: drop-shadow(0 0 10px rgba(244,114,182,0.45));
        }

        .sc-dash-text {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.35rem;
            line-height: 1;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #ffffff 0%, #f9a8d4 55%, #c4b5fd 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        </style>

        <div class="sc-dash-wrap">
            <div class="sc-dash-logo">
                <svg class="sc-dash-orbit" viewBox="0 0 58 58" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="dg1" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stop-color="#f472b6" stop-opacity="0"/>
                            <stop offset="60%" stop-color="#f472b6" stop-opacity="1"/>
                            <stop offset="100%" stop-color="#f472b6" stop-opacity="0"/>
                        </linearGradient>
                    </defs>
                    <circle cx="29" cy="29" r="26" fill="none" stroke="url(#dg1)" stroke-width="1.2" stroke-dasharray="28 135"/>
                    <circle cx="29" cy="3" r="3" fill="#f472b6"/>
                </svg>
                <svg class="sc-dash-core" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <linearGradient id="dg2" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#f472b6"/>
                            <stop offset="100%" stop-color="#7c3aed"/>
                        </linearGradient>
                    </defs>
                    <rect x="0" y="0" width="160" height="160" rx="38" fill="#0a0015"/>
                    <rect x="2" y="2" width="156" height="156" rx="36" fill="none" stroke="url(#dg2)" stroke-width="1.5" opacity="0.5"/>
                    <path d="M100 48 Q100 34 80 34 Q60 34 60 52 Q60 70 80 70 Q100 70 100 88 Q100 106 80 106 Q60 106 60 94"
                          stroke="url(#dg2)" stroke-width="7" fill="none" stroke-linecap="round"/>
                    <circle cx="104" cy="36" r="5" fill="#7c3aed" opacity="0.9"/>
                </svg>
            </div>
            <div class="sc-dash-text">PRE<br>ZENCE</div>
        </div>
    """)
