import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        stats_html = '<div style="display:flex; gap:0.6rem; flex-wrap:wrap; margin-bottom:0.25rem;">'
        for icon, label, value in stats:
            stats_html += f'<div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.07); padding:5px 12px; border-radius:0.6rem; font-size:0.82rem; font-family:DM Sans,sans-serif; color:#94a3b8; display:flex; align-items:center; gap:5px;">{icon} <span style="font-weight:600; color:#c4b5fd;">{value}</span> <span>{label}</span></div>'
        stats_html += "</div>"

    st.html(f"""
        <div style="background:linear-gradient(135deg,rgba(255,255,255,0.04) 0%,rgba(139,92,246,0.06) 100%); border:1px solid rgba(139,92,246,0.2); border-radius:1.25rem; padding:1.5rem 1.5rem 1rem; margin-bottom:1.25rem; position:relative; overflow:hidden; box-shadow:0 4px 24px rgba(0,0,0,0.3);">
            <div style="position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg,#7c3aed,#a78bfa,transparent);"></div>
            <div style="position:absolute; top:-30px; right:-30px; width:100px; height:100px; border-radius:50%; background:radial-gradient(circle,rgba(139,92,246,0.12) 0%,transparent 70%);"></div>
            <div style="font-family:Syne,sans-serif; font-weight:700; font-size:1.15rem; color:#e2e8f0; margin-bottom:0.5rem; position:relative;">{name}</div>
            <div style="display:flex; gap:0.5rem; align-items:center; margin-bottom:0.9rem;">
                <span style="font-family:monospace; font-size:0.72rem; background:rgba(139,92,246,0.15); color:#a78bfa; border:1px solid rgba(139,92,246,0.3); padding:3px 10px; border-radius:999px; letter-spacing:0.05em;">{code}</span>
                <span style="font-family:DM Sans,sans-serif; font-size:0.78rem; color:rgba(148,163,184,0.6);">· Section {section}</span>
            </div>
            {stats_html}
        </div>
    """)

    if footer_callback:
        footer_callback()