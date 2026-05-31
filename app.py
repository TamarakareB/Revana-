import io
import time
from datetime import datetime

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Keys are loaded per-module in rainforest.py and analyzer.py
# (Streamlit secrets → .env fallback)

st.set_page_config(
    page_title="Revana — Review Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* === LAYER 1: ATMOSPHERIC BACKGROUND (fix #1) === */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
.stApp {
    background:
        radial-gradient(ellipse at 0% 0%, rgba(79,70,229,0.07) 0%, transparent 50%),
        radial-gradient(ellipse at 100% 0%, rgba(6,182,212,0.06) 0%, transparent 45%),
        radial-gradient(ellipse at 50% 100%, rgba(124,58,237,0.05) 0%, transparent 50%),
        #EEF2FF !important;
    background-attachment: fixed !important;
}

/* === GLOBAL === */
html,body,[class*="css"]{font-family:'Inter',sans-serif;background-color:#EEF2FF;color:#0F172A;}
.main .block-container{padding-top:0;padding-bottom:3rem;max-width:1200px;}

/* === LAYER 2: SECTION CONTAINERS — frosted glass (fix #5) === */
.section-container{
    background:rgba(255,255,255,0.55);
    backdrop-filter:blur(8px);
    -webkit-backdrop-filter:blur(8px);
    border-radius:20px;
    padding:1.75rem;
    margin-bottom:1.5rem;
    border:1px solid rgba(255,255,255,0.8);
    box-shadow:0 2px 4px rgba(15,23,42,.04),0 0 0 1px rgba(79,70,229,.04),inset 0 1px 0 rgba(255,255,255,.9),inset 0 -1px 0 rgba(15,23,42,.03);
}

/* === SECTION DIVIDER — light beam lines (fix #11) === */
.section-divider{display:flex;align-items:center;gap:1rem;margin:2rem 0 1.5rem;}
.section-divider-line{flex:1;height:1px;background:linear-gradient(90deg,transparent 0%,rgba(79,70,229,.2) 30%,rgba(6,182,212,.3) 50%,rgba(79,70,229,.2) 70%,transparent 100%);}
.section-divider-label{font-family:'Plus Jakarta Sans',sans-serif;font-size:.72rem;font-weight:700;color:#4F46E5;text-transform:uppercase;letter-spacing:.1em;padding:4px 12px;background:#EEF2FF;border:1px solid #C7D2FE;border-radius:20px;white-space:nowrap;}

/* === LISTING BULLETS (fix #12 — shine effect) === */
.listing-bullet{background:linear-gradient(145deg,#FFFFFF,#FAFBFF);border-radius:14px;padding:0;margin-bottom:1rem;box-shadow:0 2px 8px rgba(79,70,229,.08),0 1px 2px rgba(0,0,0,.04),inset 0 1px 0 rgba(255,255,255,1);border:1px solid #E8ECFF;overflow:hidden;display:flex;transition:all .25s cubic-bezier(0.4,0,0.2,1);}
.listing-bullet:hover{box-shadow:0 8px 24px rgba(79,70,229,.15),inset 0 1px 0 rgba(255,255,255,1);transform:translateY(-2px);border-color:#C7D2FE;}
.bullet-number-strip{background:linear-gradient(160deg,#6366F1 0%,#4F46E5 40%,#4338CA 70%,#3730A3 100%);color:white;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.1rem;font-weight:800;width:52px;min-height:80px;display:flex;align-items:center;justify-content:center;flex-shrink:0;position:relative;overflow:hidden;}
.bullet-number-strip::after{content:'';position:absolute;top:0;left:0;right:0;height:40%;background:linear-gradient(180deg,rgba(255,255,255,.15) 0%,transparent 100%);pointer-events:none;}
.bullet-content{padding:1rem 1.25rem;flex:1;}
.bullet-keyword{font-family:'Plus Jakarta Sans',sans-serif;font-size:.72rem;font-weight:700;color:#4F46E5;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.3rem;}
.bullet-text{font-size:.92rem;color:#1E293B;line-height:1.65;font-weight:400;}
.bullet-copy-hint{font-size:.68rem;color:#CBD5E1;margin-top:.4rem;}

/* === TITLE COMPARISON === */
.title-compare-container{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1.5rem;}
.title-box{background:white;border-radius:14px;padding:1.25rem;box-shadow:0 2px 8px rgba(0,0,0,.06);}
.title-box-header{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.6rem;display:flex;align-items:center;gap:.4rem;}
.title-box.before .title-box-header{color:#EF4444;}
.title-box.after .title-box-header{color:#10B981;}
.title-box.before{border:1px solid #FECACA;border-top:3px solid #EF4444;}
.title-box.after{border:1px solid #A7F3D0;border-top:3px solid #10B981;}
.title-box-text{font-size:.88rem;line-height:1.6;color:#1E293B;}
.title-box.before .title-box-text{color:#94A3B8;text-decoration:line-through;text-decoration-color:#FECACA;}

/* === KEYWORD TAGS (inline chips, still used in report preview) === */
.keyword-tag{display:inline-flex;align-items:center;gap:4px;font-size:.8rem;font-weight:600;padding:6px 14px;border-radius:20px;margin:4px;cursor:default;transition:all .15s;box-shadow:0 1px 3px rgba(0,0,0,.08);}
.keyword-tag:hover{transform:translateY(-1px);box-shadow:0 3px 8px rgba(0,0,0,.12);}

/* === KEYWORD CARDS (functional 2-col grid) === */
.kw-explainer{background:linear-gradient(135deg,#EEF2FF,#ECFEFF);border:1px solid #C7D2FE;border-radius:14px;padding:1.25rem 1.5rem;margin-bottom:1.5rem;}
.kw-explainer-title{font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;color:#1E1B4B;font-size:.95rem;margin-bottom:.4rem;}
.kw-explainer-body{font-size:.85rem;color:#475569;line-height:1.6;}
.kw-card{background:linear-gradient(145deg,#FFFFFF,#FAFBFF);border-radius:14px;border:1px solid #E8ECF4;box-shadow:0 2px 8px rgba(79,70,229,.07),inset 0 1px 0 rgba(255,255,255,1);overflow:hidden;margin-bottom:.75rem;transition:all .2s cubic-bezier(0.4,0,0.2,1);}
.kw-card:hover{box-shadow:0 6px 20px rgba(79,70,229,.13);transform:translateY(-2px);border-color:#C7D2FE;}
.kw-card-top{padding:.85rem 1rem .5rem 1rem;}
.kw-card-keyword{font-family:'Plus Jakarta Sans',sans-serif;font-size:.95rem;font-weight:700;color:#0F172A;margin-bottom:.5rem;}
.kw-placement-badge{display:inline-flex;align-items:center;gap:5px;padding:2px 9px;border-radius:20px;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em;}
.kw-where{font-size:.72rem;color:#94A3B8;margin-top:.35rem;}
.kw-card-bottom{background:#F8FAFF;border-top:1px solid #EEF2FF;padding:.5rem 1rem;display:flex;align-items:center;justify-content:space-between;}
.kw-copy-hint{font-size:.68rem;color:#94A3B8;}

/* === VOC SUMMARY === */
.voc-summary{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-bottom:1.5rem;}
.voc-summary-item{background:white;border-radius:12px;padding:1rem;text-align:center;border:1px solid #E2E8F0;box-shadow:0 1px 3px rgba(15,23,42,.04);}
.voc-summary-number{font-family:'Plus Jakarta Sans',sans-serif;font-size:2rem;font-weight:800;line-height:1;}
.voc-summary-label{font-size:.72rem;color:#94A3B8;font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin-top:.3rem;}
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* === SCROLLBAR === */
::-webkit-scrollbar{width:5px;}
::-webkit-scrollbar-track{background:#EEF2FF;}
::-webkit-scrollbar-thumb{background:#CBD5E1;border-radius:3px;}
::-webkit-scrollbar-thumb:hover{background:#4F46E5;}

/* === SIDEBAR — deep space atmosphere (fix #2) === */
[data-testid="stSidebar"]{
    background:
        radial-gradient(ellipse at 50% 0%, rgba(79,70,229,0.4) 0%, transparent 60%),
        radial-gradient(ellipse at 0% 100%, rgba(6,182,212,0.15) 0%, transparent 50%),
        linear-gradient(180deg,#1E1B4B 0%,#0F172A 60%,#0C1220 100%) !important;
    border-right:1px solid rgba(255,255,255,0.06) !important;
    box-shadow:4px 0 32px rgba(0,0,0,0.2) !important;
}
[data-testid="stSidebar"] *{color:#E2E8F0!important;}
[data-testid="stSidebar"] input{background:rgba(255,255,255,.08)!important;border:1px solid rgba(255,255,255,.15)!important;color:white!important;border-radius:8px!important;}
[data-testid="stSidebar"] label{color:#94A3B8!important;}

/* === TABS — frosted glass floating bar (fix #8) === */
[data-testid="stTabs"]{
    background:rgba(255,255,255,0.7) !important;
    backdrop-filter:blur(12px) !important;
    -webkit-backdrop-filter:blur(12px) !important;
    border:1px solid rgba(255,255,255,0.9) !important;
    border-radius:14px !important;
    box-shadow:0 4px 16px rgba(79,70,229,0.08),0 1px 3px rgba(15,23,42,0.06),inset 0 1px 0 rgba(255,255,255,1) !important;
    margin-bottom:1.5rem !important;
    padding:0.3rem !important;
}
.stTabs [data-baseweb="tab-list"]{background:transparent;border-radius:14px;padding:5px;gap:3px;border:none;box-shadow:none;}
.stTabs [data-baseweb="tab"]{background:transparent;border-radius:10px;color:#475569;font-weight:500;font-size:.875rem;padding:8px 16px;border:none;transition:all .2s;font-family:'Inter',sans-serif;}
.stTabs [data-baseweb="tab"]:hover{background:#EEF2FF;color:#4F46E5;}
.stTabs [aria-selected="true"]{background:linear-gradient(135deg,#4F46E5,#7C3AED)!important;color:white!important;font-weight:600!important;box-shadow:0 2px 8px rgba(79,70,229,.3);}
.stTabs [data-baseweb="tab-panel"]{padding-top:24px;}

/* === BUTTONS === */
.stButton>button{background:linear-gradient(135deg,#4F46E5,#7C3AED);color:white;border:none;border-radius:10px;font-weight:600;font-size:.9rem;padding:10px 28px;box-shadow:0 4px 14px rgba(79,70,229,.3);transition:all .25s;font-family:'Inter',sans-serif;}
.stButton>button:hover{box-shadow:0 6px 20px rgba(79,70,229,.45);transform:translateY(-2px);}
.stButton>button:active{transform:translateY(0);box-shadow:0 2px 8px rgba(79,70,229,.3);}

/* === INPUTS === */
.stTextInput>div>div>input{background:white;border:1.5px solid #E2E8F0;border-radius:10px;color:#0F172A;font-size:.9rem;padding:10px 14px;font-family:'Inter',sans-serif;transition:all .2s;box-shadow:0 1px 2px rgba(15,23,42,.04);}
.stTextInput>div>div>input:focus{border-color:#4F46E5;box-shadow:0 0 0 3px rgba(79,70,229,.1);outline:none;}
.stTextInput>div>div>input::placeholder{color:#94A3B8;}
.stTextInput label{color:#475569!important;font-weight:600;font-size:.82rem;}
.stCheckbox label span{color:#475569!important;}
.stCheckbox label p{color:#475569!important;}

/* === PROGRESS === */
.stProgress>div>div{background:#EEF2FF!important;border-radius:6px;}
.stProgress>div>div>div>div{background:linear-gradient(90deg,#4F46E5,#7C3AED,#06B6D4)!important;border-radius:6px;}

/* === EXPANDERS === */
.streamlit-expanderHeader{background:white!important;border:1.5px solid #E2E8F0!important;border-radius:12px!important;color:#0F172A!important;font-weight:600!important;padding:14px 20px!important;box-shadow:0 1px 3px rgba(15,23,42,.06)!important;transition:all .2s!important;}
.streamlit-expanderHeader:hover{border-color:#4F46E5!important;box-shadow:0 4px 12px rgba(79,70,229,.1)!important;}
.streamlit-expanderContent{background:white!important;border:1.5px solid #E2E8F0!important;border-top:none!important;border-radius:0 0 12px 12px!important;padding:20px!important;}

/* === NATIVE METRICS === */
[data-testid="metric-container"]{background:white;border:1px solid #E2E8F0;border-radius:16px;padding:20px;box-shadow:0 1px 3px rgba(15,23,42,.06),0 4px 16px rgba(15,23,42,.04);}
[data-testid="stMetricValue"]{color:#0F172A!important;font-size:1.9rem!important;font-weight:700!important;font-family:'Plus Jakarta Sans',sans-serif!important;}
[data-testid="stMetricLabel"]{color:#94A3B8!important;font-size:.72rem!important;text-transform:uppercase;letter-spacing:.5px;font-weight:600!important;}
[data-testid="stMetricDelta"]{font-size:.8rem!important;}

/* === ALERTS === */
.stSuccess{background:#ECFDF5!important;border-left:4px solid #10B981!important;border-radius:0 12px 12px 0!important;}
.stInfo{background:#EEF2FF!important;border-left:4px solid #4F46E5!important;border-radius:0 12px 12px 0!important;}
.stWarning{background:#FFFBEB!important;border-left:4px solid #F59E0B!important;border-radius:0 12px 12px 0!important;}
.stError{background:#FEF2F2!important;border-left:4px solid #EF4444!important;border-radius:0 12px 12px 0!important;}

/* === DATAFRAME & CODE === */
.stDataFrame{border:1px solid #E2E8F0;border-radius:12px;overflow:hidden;}

/* === HEADER — glassmorphism + glow line (fix #3) === */
.revana-header{
    background:linear-gradient(135deg,#4338CA 0%,#6D28D9 40%,#0891B2 100%);
    padding:2.5rem 3rem;margin:0 0 2rem 0;position:relative;overflow:hidden;
    border-bottom:1px solid rgba(255,255,255,.1);
    box-shadow:0 4px 32px rgba(79,70,229,.25),inset 0 1px 0 rgba(255,255,255,.1),inset 0 -1px 0 rgba(0,0,0,.1);
}
.revana-header::before{content:'';position:absolute;top:-60%;right:-5%;width:350px;height:350px;background:radial-gradient(circle,rgba(255,255,255,.12) 0%,transparent 65%);border-radius:50%;pointer-events:none;}
.revana-header::after{content:'';position:absolute;bottom:-80%;left:30%;width:280px;height:280px;background:radial-gradient(circle,rgba(6,182,212,.2) 0%,transparent 65%);border-radius:50%;pointer-events:none;}
.revana-header-glow{position:absolute;bottom:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent 0%,rgba(255,255,255,.4) 30%,rgba(6,182,212,.6) 50%,rgba(255,255,255,.4) 70%,transparent 100%);}
.revana-logo{font-family:'Plus Jakarta Sans',sans-serif;font-size:2.8rem;font-weight:800;color:white;letter-spacing:-.03em;line-height:1;margin-bottom:.4rem;}
.revana-tagline{font-size:1rem;color:rgba(255,255,255,.8);font-weight:400;margin-bottom:1rem;}
.revana-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.2);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.3);color:white;font-size:.72rem;font-weight:600;padding:4px 12px;border-radius:20px;letter-spacing:.06em;text-transform:uppercase;}

/* === HEALTH CONTAINER — glowing ring (fix #7) === */
.health-container{background:linear-gradient(145deg,#FFFFFF 0%,#F8FAFF 100%);border-radius:20px;padding:2.5rem 2rem;text-align:center;border:1px solid #E8ECF4;position:relative;overflow:hidden;box-shadow:0 2px 8px rgba(15,23,42,.06),inset 0 1px 0 rgba(255,255,255,1);}
.health-container::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:160px;height:160px;border-radius:50%;pointer-events:none;transition:background .3s;}
.health-container.good::before{background:radial-gradient(circle,rgba(16,185,129,.12) 0%,transparent 70%);box-shadow:0 0 60px rgba(16,185,129,.1);}
.health-container.medium::before{background:radial-gradient(circle,rgba(245,158,11,.12) 0%,transparent 70%);box-shadow:0 0 60px rgba(245,158,11,.1);}
.health-container.poor::before{background:radial-gradient(circle,rgba(239,68,68,.12) 0%,transparent 70%);box-shadow:0 0 60px rgba(239,68,68,.1);}
.health-score-number{font-family:'Plus Jakarta Sans',sans-serif;font-size:5.5rem;font-weight:800;line-height:1;position:relative;z-index:1;letter-spacing:-.04em;}
.health-good{color:#10B981;text-shadow:0 0 40px rgba(16,185,129,.3);}
.health-medium{color:#F59E0B;text-shadow:0 0 40px rgba(245,158,11,.3);}
.health-poor{color:#EF4444;text-shadow:0 0 40px rgba(239,68,68,.3);}

/* === INSIGHT CARDS — dimensional presence (fix #6) === */
.insight-card{background:linear-gradient(145deg,#FFFFFF 0%,#FAFBFF 100%);border:1px solid #E8ECF4;border-radius:14px;padding:1.25rem 1.5rem;margin-bottom:.75rem;box-shadow:0 1px 3px rgba(15,23,42,.06),0 4px 12px rgba(15,23,42,.04),inset 0 1px 0 rgba(255,255,255,1);transition:all .25s cubic-bezier(0.4,0,0.2,1);}
.insight-card.complaint:hover{box-shadow:0 8px 24px rgba(239,68,68,.12),0 2px 8px rgba(239,68,68,.08),inset 0 1px 0 rgba(255,255,255,1);border-color:#FECACA;transform:translateY(-2px) translateX(2px);}
.insight-card.praise:hover{box-shadow:0 8px 24px rgba(16,185,129,.12),0 2px 8px rgba(16,185,129,.08),inset 0 1px 0 rgba(255,255,255,1);border-color:#A7F3D0;transform:translateY(-2px) translateX(2px);}

/* === PERSONA === */
.persona-card{background:white;border:1.5px solid #E2E8F0;border-radius:16px;padding:24px;margin-bottom:20px;box-shadow:0 1px 3px rgba(15,23,42,.06),0 4px 16px rgba(79,70,229,.06),inset 0 1px 0 rgba(255,255,255,1);transition:all .25s cubic-bezier(0.4,0,0.2,1);}
.persona-card:hover{border-color:#4F46E5;box-shadow:0 4px 12px rgba(15,23,42,.08),0 12px 32px rgba(79,70,229,.12);transform:translateY(-2px);}

/* === METRIC CARDS — colored glow shadows (fix #4) === */
.metric-card{background:linear-gradient(145deg,#ffffff 0%,#FAFBFF 100%);border:1px solid #E2E8F0;border-radius:16px;padding:1.5rem;position:relative;overflow:hidden;transition:all .25s cubic-bezier(0.4,0,0.2,1);}
.metric-card::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;border-radius:16px 16px 0 0;}
.metric-card.indigo::after{background:linear-gradient(90deg,#4F46E5,#7C3AED);}
.metric-card.indigo{box-shadow:0 1px 2px rgba(0,0,0,.04),0 4px 16px rgba(79,70,229,.1),inset 0 0 0 1px rgba(79,70,229,.08);}
.metric-card.indigo:hover{box-shadow:0 8px 32px rgba(79,70,229,.18),0 2px 8px rgba(79,70,229,.12),inset 0 0 0 1px rgba(79,70,229,.12);transform:translateY(-3px);}
.metric-card.cyan::after{background:linear-gradient(90deg,#06B6D4,#0EA5E9);}
.metric-card.cyan{box-shadow:0 1px 2px rgba(0,0,0,.04),0 4px 16px rgba(6,182,212,.1),inset 0 0 0 1px rgba(6,182,212,.08);}
.metric-card.cyan:hover{box-shadow:0 8px 32px rgba(6,182,212,.18),0 2px 8px rgba(6,182,212,.12),inset 0 0 0 1px rgba(6,182,212,.12);transform:translateY(-3px);}
.metric-card.green::after{background:linear-gradient(90deg,#10B981,#059669);}
.metric-card.green{box-shadow:0 1px 2px rgba(0,0,0,.04),0 4px 16px rgba(16,185,129,.1),inset 0 0 0 1px rgba(16,185,129,.08);}
.metric-card.green:hover{box-shadow:0 8px 32px rgba(16,185,129,.18),inset 0 0 0 1px rgba(16,185,129,.12);transform:translateY(-3px);}
.metric-card.amber::after{background:linear-gradient(90deg,#F59E0B,#EF4444);}
.metric-card.amber{box-shadow:0 1px 2px rgba(0,0,0,.04),0 4px 16px rgba(245,158,11,.1),inset 0 0 0 1px rgba(245,158,11,.08);}
.metric-card.amber:hover{box-shadow:0 8px 32px rgba(245,158,11,.18),inset 0 0 0 1px rgba(245,158,11,.12);transform:translateY(-3px);}
.metric-icon{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;margin-bottom:.75rem;}
.metric-icon.indigo{background:#EEF2FF;}
.metric-icon.cyan{background:#ECFEFF;}
.metric-icon.green{background:#ECFDF5;}
.metric-icon.amber{background:#FFFBEB;}
.metric-label{font-size:.7rem;font-weight:600;color:#94A3B8;text-transform:uppercase;letter-spacing:.5px;margin-bottom:.25rem;}
.metric-value{font-family:'Plus Jakarta Sans',sans-serif;font-size:1.9rem;font-weight:800;color:#0F172A;line-height:1;}
.metric-sub{font-size:.78rem;color:#94A3B8;margin-top:.3rem;}

/* === CONTENT CARDS === */
.section-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:1.05rem;font-weight:700;color:#0F172A;padding-bottom:12px;border-bottom:1.5px solid #E2E8F0;margin-bottom:20px;}
.callout{background:#EEF2FF;border-left:4px solid #4F46E5;border-radius:0 10px 10px 0;padding:16px 20px;margin:12px 0;color:#3730A3;line-height:1.7;font-size:.9rem;}
.callout-green{background:#ECFDF5;border-left:4px solid #10B981;border-radius:0 10px 10px 0;padding:14px 18px;margin:10px 0;color:#065F46;line-height:1.65;font-size:.875rem;}
.callout-red{background:#FEF2F2;border-left:4px solid #EF4444;border-radius:0 10px 10px 0;padding:14px 18px;margin:10px 0;color:#7F1D1D;line-height:1.65;font-size:.875rem;}
.callout-yellow{background:#FFFBEB;border-left:4px solid #F59E0B;border-radius:0 10px 10px 0;padding:14px 18px;margin:10px 0;color:#78350F;line-height:1.65;font-size:.875rem;}
.quote-box{background:#F8FAFF;border-left:3px solid #4F46E5;border-radius:0 8px 8px 0;padding:12px 16px;margin:8px 0;font-style:italic;color:#4338CA;font-size:.875rem;line-height:1.6;}
.badge{display:inline-block;padding:2px 10px;border-radius:20px;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.4px;}
.badge-critical{background:#FEE2E2;color:#DC2626;}
.badge-high{background:#FEF3C7;color:#D97706;}
.badge-medium{background:#FEF9C3;color:#CA8A04;}
.badge-low{background:#D1FAE5;color:#059669;}
.tag{display:inline-block;background:#EEF2FF;border:1px solid #C7D2FE;color:#4338CA;border-radius:20px;padding:4px 14px;font-size:.78rem;margin:3px;font-weight:500;}

/* === HEALTH SCORE === */
.health-wrap{background:white;border:1px solid #E2E8F0;border-radius:20px;padding:28px;text-align:center;box-shadow:0 1px 3px rgba(15,23,42,.06);}
.health-val{font-family:'Plus Jakarta Sans',sans-serif;font-size:4.5rem;font-weight:900;line-height:1;margin:8px 0;}
.health-lbl{font-size:.7rem;color:#94A3B8;text-transform:uppercase;letter-spacing:1px;font-weight:600;}

/* === GAP CARDS === */
.adv-card{background:#ECFDF5;border:1.5px solid #6EE7B7;border-radius:14px;padding:20px;margin-bottom:14px;}
.vuln-card{background:#FEF2F2;border:1.5px solid #FECACA;border-radius:14px;padding:20px;margin-bottom:14px;}

/* persona-card defined above in INSIGHT CARDS section */

/* === MISC === */
.mini-label{font-size:.7rem;color:#94A3B8;text-transform:uppercase;letter-spacing:.5px;font-weight:600;margin-bottom:6px;}
.empty-state{text-align:center;padding:80px 20px;color:#94A3B8;}
.empty-state .icon{font-size:3rem;margin-bottom:16px;}
.empty-state h3{color:#475569!important;font-family:'Plus Jakarta Sans',sans-serif!important;}
.footer{text-align:center;padding:32px 0 16px 0;border-top:1px solid #E2E8F0;margin-top:48px;color:#94A3B8;font-size:.78rem;}
hr{border-color:#E2E8F0!important;margin:24px 0;}
.powered-badge{display:inline-flex;align-items:center;gap:6px;background:#EEF2FF;border:1px solid #C7D2FE;color:#4338CA;font-size:.72rem;font-weight:600;padding:4px 12px;border-radius:20px;letter-spacing:.06em;text-transform:uppercase;}

/* === STEP CARDS (how it works) === */
.step-card{background:white;border:1px solid #E2E8F0;border-radius:14px;padding:20px 16px;text-align:center;height:170px;box-shadow:0 1px 3px rgba(15,23,42,.06);transition:all .2s;}
.step-card:hover{border-color:#4F46E5;box-shadow:0 4px 16px rgba(79,70,229,.1);transform:translateY(-2px);}

/* === REPORT PREVIEW — paper depth (fix #9) === */
.report-preview{background:white;border-radius:16px;box-shadow:0 2px 4px rgba(15,23,42,.04),0 8px 24px rgba(79,70,229,.08),0 24px 64px rgba(15,23,42,.08),0 0 0 1px rgba(79,70,229,.06);overflow:hidden;max-width:780px;margin:0 auto;position:relative;}
.report-preview::before{content:'';position:absolute;top:5%;bottom:5%;left:-8px;width:16px;background:linear-gradient(90deg,transparent 0%,rgba(15,23,42,.04) 50%,transparent 100%);filter:blur(4px);pointer-events:none;}
.report-header{background:linear-gradient(135deg,#4F46E5 0%,#7C3AED 50%,#06B6D4 100%);padding:2rem 2.5rem;color:white;position:relative;overflow:hidden;}
.report-header::before{content:'';position:absolute;top:-40%;right:-5%;width:200px;height:200px;background:rgba(255,255,255,.08);border-radius:50%;}
.report-brand{font-family:'Plus Jakarta Sans',sans-serif;font-size:1rem;font-weight:800;letter-spacing:.15em;text-transform:uppercase;opacity:.9;margin-bottom:.5rem;}
.report-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:1.5rem;font-weight:700;margin-bottom:.25rem;line-height:1.3;}
.report-subtitle{font-size:.85rem;opacity:.75;}
.report-meta{display:flex;gap:1.5rem;margin-top:1rem;flex-wrap:wrap;}
.report-meta-item{font-size:.75rem;opacity:.8;}
.report-meta-item span{font-weight:700;opacity:1;}
.report-body{padding:2rem 2.5rem;}
.report-section{margin-bottom:1.75rem;}
.report-section-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:#4F46E5;margin-bottom:.75rem;padding-bottom:.4rem;border-bottom:2px solid #EEF2FF;}
.report-summary-text{font-size:.9rem;color:#334155;line-height:1.75;background:#F8FAFC;border-left:3px solid #4F46E5;padding:.85rem 1.1rem;border-radius:0 8px 8px 0;}
.report-complaint-row{display:flex;align-items:flex-start;gap:1rem;padding:.75rem 0;border-bottom:1px solid #F1F5F9;}
.report-complaint-row:last-child{border-bottom:none;}
.report-complaint-rank{width:28px;height:28px;background:linear-gradient(135deg,#EF4444,#F87171);color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:2px;}
.report-complaint-rank.praise{background:linear-gradient(135deg,#10B981,#34D399);}
.report-complaint-theme{font-weight:600;font-size:.88rem;color:#1E293B;margin-bottom:.2rem;}
.report-complaint-meta{font-size:.75rem;color:#94A3B8;margin-bottom:.2rem;}
.report-complaint-rec{font-size:.8rem;color:#64748B;line-height:1.5;}
.report-bullet-preview{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:8px;padding:.65rem 1rem;font-size:.82rem;color:#334155;margin-bottom:.4rem;line-height:1.5;display:flex;gap:.75rem;}
.report-bullet-num{color:#4F46E5;font-weight:700;flex-shrink:0;}
.report-footer-bar{background:#F8FAFC;border-top:1px solid #E2E8F0;padding:1rem 2.5rem;display:flex;align-items:center;justify-content:space-between;}
.report-footer-brand{font-family:'Plus Jakarta Sans',sans-serif;font-size:.75rem;font-weight:700;color:#4F46E5;letter-spacing:.05em;}
.report-footer-meta{font-size:.72rem;color:#94A3B8;}

/* === EXPORT DOWNLOAD CARDS === */
.export-card{background:white;border:1.5px solid #E2E8F0;border-radius:16px;padding:1.5rem;box-shadow:0 1px 3px rgba(15,23,42,.06),0 4px 16px rgba(79,70,229,.06);transition:all .2s;text-align:center;}
.export-card:hover{border-color:#4F46E5;box-shadow:0 4px 12px rgba(15,23,42,.08),0 12px 32px rgba(79,70,229,.12);transform:translateY(-2px);}
.export-icon{font-size:2.2rem;margin-bottom:.75rem;}
.export-title{font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;color:#0F172A;font-size:.95rem;margin-bottom:.3rem;}
.export-desc{color:#94A3B8;font-size:.78rem;line-height:1.4;margin-bottom:.75rem;}

/* === COMPETITOR HEADER === */
.comp-card-mine{background:white;border:2px solid #4F46E5;border-radius:14px;padding:20px;}
.comp-card-comp{background:white;border:2px solid #F59E0B;border-radius:14px;padding:20px;}

/* === PRODUCT HEADER === */
.product-pill{display:inline-block;background:#EEF2FF;border:1px solid #C7D2FE;color:#4338CA;font-size:.75rem;font-weight:600;padding:3px 12px;border-radius:20px;margin-right:6px;}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────
_DEFAULTS = dict(
    analyzed=False, product_info=None, reviews_df=None,
    trusted_reviews=None, filter_stats=None, analysis=None,
    trends=None, rating_distribution=None,
    has_competitor=False, competitor=None, gap_analysis=None,
)
for _k, _v in _DEFAULTS.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

# ── Design tokens ─────────────────────────────────────────────────────────
_INDIGO  = "#4F46E5"
_VIOLET  = "#7C3AED"
_CYAN    = "#06B6D4"
_GREEN   = "#10B981"
_AMBER   = "#F59E0B"
_RED     = "#EF4444"
_DARK    = "#0F172A"
_SLATE   = "#475569"
_MUTED   = "#94A3B8"
_BORDER  = "#E2E8F0"
_BG_CARD = "rgba(248,250,255,0.7)"
_GRID    = "#E2E8F0"
_FONT    = dict(color=_SLATE, family="Inter, sans-serif", size=11)
_FONT_HED = dict(color=_DARK, family="Plus Jakarta Sans, sans-serif", size=12)

# ── Plotly base layout ────────────────────────────────────────────────────
def _base_layout(**kw):
    base = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#F8FAFF",
        font=_FONT,
        margin=dict(l=8, r=8, t=44, b=8),
        xaxis=dict(gridcolor=_GRID, linecolor=_BORDER, tickcolor=_BORDER,
                   tickfont=_FONT, title_font=_FONT),
        yaxis=dict(gridcolor=_GRID, linecolor=_BORDER, tickcolor=_BORDER,
                   tickfont=_FONT, title_font=_FONT),
        legend=dict(bgcolor="rgba(255,255,255,0.95)", bordercolor=_BORDER,
                    borderwidth=1, font=_FONT),
        title=dict(font=dict(color=_DARK, family="Plus Jakarta Sans, sans-serif", size=14),
                   x=0, pad=dict(l=4)),
    )
    base.update(kw)
    return base

# ── Chart builders ────────────────────────────────────────────────────────
def chart_rating_dist(dist: dict) -> go.Figure:
    stars  = ["⭐ 5 stars", "⭐ 4 stars", "⭐ 3 stars", "⭐ 2 stars", "⭐ 1 star"]
    keys   = ["5", "4", "3", "2", "1"]
    pcts   = [dist.get(k, {}).get("percentage", 0) for k in keys]
    counts = [dist.get(k, {}).get("count", 0) for k in keys]
    colors = [_INDIGO, "#818CF8", _AMBER, "#FB923C", _RED]
    fig = go.Figure(go.Bar(
        x=pcts, y=stars, orientation="h",
        marker=dict(color=colors, line=dict(width=0)),
        customdata=counts,
        text=[f"{p:.1f}%" for p in pcts],
        textposition="outside",
        textfont=dict(color=_SLATE, size=11),
        hovertemplate="%{y}: <b>%{x:.1f}%</b> (%{customdata} reviews)<extra></extra>",
    ))
    fig.update_layout(**_base_layout(
        title="Rating Distribution", height=230,
        xaxis=dict(range=[0, 110], gridcolor=_GRID, linecolor=_BORDER,
                   tickcolor=_BORDER, ticksuffix="%", tickfont=_FONT),
        yaxis=dict(gridcolor=_GRID, linecolor=_BORDER, tickcolor=_BORDER, tickfont=_FONT),
    ))
    return fig


def chart_trends_line(monthly: list) -> go.Figure:
    valid   = [m for m in monthly if m.get("average_rating") is not None]
    months  = [m["month"] for m in valid]
    ratings = [m["average_rating"] for m in valid]
    complaints = [m.get("complaint_rate", 0) for m in valid]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=ratings, mode="lines+markers", name="Avg Rating",
        line=dict(color=_INDIGO, width=3),
        marker=dict(color=_INDIGO, size=8, line=dict(color="white", width=2)),
        fill="tozeroy", fillcolor="rgba(79,70,229,0.07)",
        hovertemplate="%{x}<br><b>Rating: %{y:.2f}★</b><extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=months, y=complaints, mode="lines+markers", name="Complaint %",
        line=dict(color=_RED, width=2, dash="dot"),
        marker=dict(color=_RED, size=6, line=dict(color="white", width=2)),
        yaxis="y2",
        hovertemplate="%{x}<br><b>Complaints: %{y:.1f}%</b><extra></extra>",
    ))
    fig.add_hline(y=4.0, line_dash="dot", line_color="rgba(245,158,11,0.5)",
                  annotation_text="4.0★ threshold",
                  annotation_font_color=_AMBER, annotation_font_size=10)
    fig.update_layout(**_base_layout(
        title="Rating & Complaint Rate Over Time", height=300,
        yaxis=dict(range=[1, 5.3], title="Avg Rating", gridcolor=_GRID,
                   linecolor=_BORDER, tickcolor=_BORDER, tickfont=_FONT, title_font=_FONT),
        yaxis2=dict(range=[0, 105], title="Complaint %", overlaying="y", side="right",
                    gridcolor="rgba(0,0,0,0)", ticksuffix="%", tickfont=_FONT, title_font=_FONT),
    ))
    return fig


def chart_volume_bar(monthly: list, spike_months: list | None = None) -> go.Figure:
    spike_months = spike_months or []
    months = [m["month"] for m in monthly]
    counts = [m["review_count"] for m in monthly]
    colors = [_RED if m["month"] in spike_months else _CYAN for m in monthly]
    fig = go.Figure(go.Bar(
        x=months, y=counts,
        marker=dict(color=colors, line=dict(width=0), opacity=0.85),
        hovertemplate="%{x}<br><b>%{y} reviews</b><extra></extra>",
    ))
    fig.update_layout(**_base_layout(title="Review Volume by Month", height=250))
    return fig


def chart_head_to_head(scores: dict, my_name: str, comp_name: str) -> go.Figure:
    cats  = ["Quality", "Value for Money", "Customer Service", "Shipping &<br>Packaging", "Ease of Use"]
    keys  = ["quality_perception", "value_for_money", "customer_service", "shipping_packaging", "ease_of_use"]
    mine  = [scores[k]["mine"] for k in keys]
    theirs = [scores[k]["competitor"] for k in keys]
    cats_c  = cats + [cats[0]]
    mine_c  = mine  + [mine[0]]
    their_c = theirs + [theirs[0]]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=mine_c, theta=cats_c, fill="toself", name=my_name[:22],
        line=dict(color=_INDIGO, width=2.5),
        fillcolor="rgba(79,70,229,0.18)",
        hovertemplate="%{theta}: <b>%{r}/10</b><extra></extra>",
    ))
    fig.add_trace(go.Scatterpolar(
        r=their_c, theta=cats_c, fill="toself", name=comp_name[:22],
        line=dict(color=_AMBER, width=2.5),
        fillcolor="rgba(245,158,11,0.12)",
        hovertemplate="%{theta}: <b>%{r}/10</b><extra></extra>",
    ))
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(248,250,255,0.9)",
            radialaxis=dict(visible=True, range=[0, 10], gridcolor=_GRID,
                            linecolor=_BORDER, tickfont=_FONT),
            angularaxis=dict(gridcolor=_GRID, linecolor=_BORDER, tickfont=_FONT),
        ),
        paper_bgcolor="rgba(0,0,0,0)", font=_FONT, height=380,
        legend=dict(bgcolor="rgba(255,255,255,0.95)", bordercolor=_BORDER, borderwidth=1, font=_FONT),
        title=dict(text="Head-to-Head Scores", font=_FONT_HED, x=0),
        margin=dict(l=40, r=40, t=50, b=40),
    )
    return fig


def chart_scores_bar(scores: dict, my_name: str, comp_name: str) -> go.Figure:
    labels = ["Quality", "Value for Money", "Customer Service", "Shipping/Pkg", "Ease of Use"]
    keys   = ["quality_perception", "value_for_money", "customer_service", "shipping_packaging", "ease_of_use"]
    mine   = [scores[k]["mine"] for k in keys]
    theirs = [scores[k]["competitor"] for k in keys]
    fig = go.Figure()
    fig.add_trace(go.Bar(name=my_name[:22], x=labels, y=mine, marker_color=_INDIGO,
                         marker_line_width=0, hovertemplate="%{x}: <b>%{y}/10</b><extra></extra>"))
    fig.add_trace(go.Bar(name=comp_name[:22], x=labels, y=theirs, marker_color=_AMBER,
                         marker_line_width=0, hovertemplate="%{x}: <b>%{y}/10</b><extra></extra>"))
    fig.update_layout(**_base_layout(title="Score Breakdown", height=300, barmode="group",
                                     yaxis=dict(range=[0, 11], gridcolor=_GRID, linecolor=_BORDER,
                                                tickcolor=_BORDER, tickfont=_FONT)))
    return fig

# ── HTML helpers ──────────────────────────────────────────────────────────
def badge_html(level: str) -> str:
    l = (level or "low").lower()
    return f'<span class="badge badge-{l}">{l}</span>'

def health_color(score: int) -> str:
    if score >= 70: return _GREEN
    if score >= 45: return _AMBER
    return _RED

def health_label(score: int) -> str:
    if score >= 70: return "Excellent"
    if score >= 45: return "Needs Work"
    return "At Risk"

def metric_card_html(icon: str, label: str, value: str, color: str = "indigo",
                     sub: str = "") -> str:
    sub_html = f'<div class="metric-sub">{sub}</div>' if sub else ""
    return f"""
    <div class="metric-card {color}">
        <div class="metric-icon {color}">{icon}</div>
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {sub_html}
    </div>"""

def empty_state(icon: str, title: str, body: str):
    st.markdown(f"""
    <div class="empty-state">
        <div class="icon">{icon}</div>
        <h3>{title}</h3>
        <p>{body}</p>
    </div>""", unsafe_allow_html=True)

# ── Report exporter ───────────────────────────────────────────────────────
def build_text_report() -> str:
    ss = st.session_state
    a  = ss.analysis
    pi = ss.product_info
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "═" * 62, "  REVANA — VOICE OF CUSTOMER BRIEF",
        f"  Generated: {now}", "═" * 62, "",
        f"PRODUCT : {pi.get('title', 'N/A')}",
        f"ASIN    : {pi.get('asin', 'N/A')}",
        f"RATING  : {pi.get('overall_rating', 'N/A')}/5  |  Total reviews: {pi.get('total_reviews', 'N/A')}",
        f"HEALTH SCORE: {a.get('overall_health_score', 'N/A')}/100", "",
        "EXECUTIVE SUMMARY", "─" * 50, a.get("executive_summary", ""), "",
    ]
    if a.get("risk_alerts"):
        lines += ["RISK ALERTS", "─" * 50]
        for r in a["risk_alerts"]:
            lines += [f"  [{r['severity'].upper()}] {r['alert_type']}",
                      f"  {r['description']}",
                      f"  → {r['recommended_action']}", ""]
    if a.get("complaint_themes"):
        lines += ["COMPLAINT THEMES", "─" * 50]
        for i, t in enumerate(a["complaint_themes"], 1):
            lines += [f"{i}. {t['theme']}  ({t['frequency_pct']}%)  [{t['emotional_intensity'].upper()}]",
                      f"   Fix: {t['improvement_recommendation']}",
                      f"   Impact: {t['estimated_rating_impact']}", ""]
    if a.get("praise_themes"):
        lines += ["PRAISE THEMES", "─" * 50]
        for i, t in enumerate(a["praise_themes"], 1):
            lines += [f"{i}. {t['theme']}  ({t['frequency_pct']}%)",
                      f"   Angle: {t['marketing_angle']}", ""]
    if a.get("listing_bullets"):
        lines += ["OPTIMIZED LISTING BULLETS", "─" * 50]
        lines += [f"• {b}" for b in a["listing_bullets"]]
        lines.append("")
    if a.get("listing_title_suggestion"):
        lines += ["SUGGESTED TITLE", "─" * 50, a["listing_title_suggestion"], ""]
    if a.get("buyer_personas"):
        lines += ["BUYER PERSONAS", "─" * 50]
        for p in a["buyer_personas"]:
            lines += [f"  {p['persona_name']} ({p.get('percentage', '?')}%)",
                      f"  {p['description']}",
                      f"  Loves: {p['what_they_love']}",
                      f"  Friction: {p['what_frustrates_them']}",
                      f"  Message: {p['marketing_message']}", ""]
    if a.get("keyword_opportunities"):
        lines += ["KEYWORD OPPORTUNITIES", "─" * 50,
                  ",  ".join(a["keyword_opportunities"]), ""]
    lines += ["─" * 62, "Powered by Revana  ×  Claude AI  ×  Anthropic", "─" * 62]
    return "\n".join(lines)

# ── Analysis runner ───────────────────────────────────────────────────────
def run_analysis(asin: str, comp_asin: str, demo: bool):
    prog   = st.progress(0)
    status = st.empty()

    def step(pct: int, msg: str):
        prog.progress(pct)
        status.markdown(
            f'<p style="color:{_SLATE};font-size:.875rem;margin:.5rem 0;">⏳ &nbsp;{msg}</p>',
            unsafe_allow_html=True,
        )
        if demo:
            time.sleep(0.4)

    try:
        if demo:
            step(15, "Loading demo product data…")
            from demo_data import get_demo_data
            data = get_demo_data(1)
            step(38, "Filtering reviews with authenticity heuristics…")
            step(58, "Running Claude AI analysis…")
            step(78, "Building buyer personas and risk alerts…")
            step(92, "Preparing competitor gap analysis…")
            st.session_state.product_info        = data["product_info"]
            st.session_state.reviews_df          = data["reviews_df"]
            st.session_state.trusted_reviews     = data["trusted_reviews"]
            st.session_state.filter_stats        = data["filter_stats"]
            st.session_state.analysis            = data["analysis"]
            st.session_state.trends              = data["trends"]
            st.session_state.rating_distribution = data["rating_distribution"]
            st.session_state.has_competitor      = True
            st.session_state.competitor          = data["competitor"]
            st.session_state.gap_analysis        = data["gap_analysis"]
        else:
            from rainforest import fetch_product_reviews
            from utils import filter_fake_reviews, compute_sentiment_trends, compute_rating_distribution
            from analyzer import analyze_reviews, competitor_gap_analysis

            step(10, "Fetching product data from Amazon…")
            result = fetch_product_reviews(asin)
            pi, df = result["product_info"], result["reviews"]

            step(30, "Filtering fake and untrustworthy reviews…")
            trusted, _, stats = filter_fake_reviews(df)
            trends = compute_sentiment_trends(df)
            dist   = compute_rating_distribution(df)

            step(55, "Running Claude AI deep analysis…")
            analysis = analyze_reviews(pi, trusted)

            st.session_state.product_info        = pi
            st.session_state.reviews_df          = df
            st.session_state.trusted_reviews     = trusted
            st.session_state.filter_stats        = stats
            st.session_state.analysis            = analysis
            st.session_state.trends              = trends
            st.session_state.rating_distribution = dist

            if comp_asin.strip():
                step(72, "Fetching competitor data…")
                cr = fetch_product_reviews(comp_asin)
                comp_pi, comp_df = cr["product_info"], cr["reviews"]
                comp_trusted, _, comp_stats = filter_fake_reviews(comp_df)
                step(88, "Running competitor gap analysis…")
                gap = competitor_gap_analysis(pi, trusted, comp_pi, comp_trusted)
                st.session_state.has_competitor = True
                st.session_state.competitor = {
                    "product_info": comp_pi, "reviews_df": comp_df,
                    "trusted_reviews": comp_trusted, "filter_stats": comp_stats,
                    "trends": compute_sentiment_trends(comp_df),
                    "rating_distribution": compute_rating_distribution(comp_df),
                }
                st.session_state.gap_analysis = gap
            else:
                st.session_state.has_competitor = False
                st.session_state.competitor     = None
                st.session_state.gap_analysis   = None

        step(100, "Analysis complete!")
        st.session_state.analyzed = True
        prog.empty(); status.empty()
        st.success("✅ Analysis complete — explore the tabs above to see your insights.")

    except Exception as e:
        prog.empty(); status.empty()
        st.error(f"Analysis failed: {e}")
        st.info("💡 Enable **Demo Mode** to explore a full example without API keys.")

# ── Tab renderers ─────────────────────────────────────────────────────────

def tab_overview():
    if not st.session_state.analyzed:
        empty_state("📊", "No analysis yet",
                    "Enter an ASIN in the Analyze tab and click Run Analysis to get started.")
        return

    a    = st.session_state.analysis
    pi   = st.session_state.product_info
    fs   = st.session_state.filter_stats
    dist = st.session_state.rating_distribution

    # ── Product header ──
    st.markdown(f"""
    <div style="margin-bottom:8px;">
        <h2 style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1.4rem;
                   font-weight:800;color:#0F172A;margin-bottom:8px;">
            {pi.get('title','Product')[:90]}{'…' if len(pi.get('title',''))>90 else ''}
        </h2>
        <span class="product-pill">ASIN: {pi.get('asin')}</span>
        <span class="product-pill">⭐ {pi.get('overall_rating')}/5</span>
        <span class="product-pill">{pi.get('total_reviews',0):,} total reviews</span>
    </div>""", unsafe_allow_html=True)

    # ── Metric cards ──
    m1, m2, m3, m4 = st.columns(4, gap="medium")
    m1.markdown(metric_card_html("⭐", "Overall Rating",
                                 f"{pi.get('overall_rating','N/A')}", "indigo",
                                 "Amazon public rating"), unsafe_allow_html=True)
    m2.markdown(metric_card_html("✅", "Trusted Reviews",
                                 str(fs.get("trusted_count", 0)), "cyan",
                                 f"of {fs.get('total_reviews_analyzed',0)} analyzed"),
                unsafe_allow_html=True)
    m3.markdown(metric_card_html("🤖", "Fake Filtered",
                                 str(fs.get("flagged_count", 0)), "amber",
                                 f"{fs.get('fake_percentage',0)}% noise removed"),
                unsafe_allow_html=True)
    score = a.get("overall_health_score", 0)
    m4.markdown(metric_card_html("💡", "Health Score",
                                 f"{score}/100", "green",
                                 health_label(score)), unsafe_allow_html=True)


    left, right = st.columns([1, 2], gap="large")

    with left:
        label = health_label(score)
        health_level = "good" if score >= 70 else "medium" if score >= 45 else "poor"
        health_cls   = f"health-{health_level}"
        summary_snip = a.get("executive_summary", "")[:90]
        st.markdown(f"""
        <div class="health-container {health_level}">
            <div class="metric-label" style="margin-bottom:.75rem;">Product Health Score</div>
            <div class="health-score-number {health_cls}">{score}</div>
            <div style="font-size:.75rem;color:#94A3B8;margin-top:.4rem;font-weight:600;
                        text-transform:uppercase;letter-spacing:.5px;">out of 100</div>
            <div style="margin-top:1rem;font-size:.82rem;color:#64748B;line-height:1.6;
                        max-width:200px;margin-left:auto;margin-right:auto;">
                {summary_snip}…
            </div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
        st.plotly_chart(chart_rating_dist(dist), use_container_width=True,
                        config={"displayModeBar": False})

    with right:
        st.markdown('<div class="section-title">Executive Summary</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="callout">{a.get("executive_summary","")}</div>',
                    unsafe_allow_html=True)
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">Risk Alerts</div>', unsafe_allow_html=True)
        sev_style = {
            "critical": ("callout-red",   "#EF4444"),
            "high":     ("callout-yellow", "#D97706"),
            "medium":   ("callout-yellow", "#F59E0B"),
            "low":      ("callout-green",  "#10B981"),
        }
        for r in a.get("risk_alerts", []):
            sev = r.get("severity", "low").lower()
            cls, border = sev_style.get(sev, ("callout", _INDIGO))
            st.markdown(f"""
            <div class="{cls}" style="border-left-color:{border};">
                {badge_html(sev)} &nbsp;
                <strong style="color:#0F172A;">{r.get('alert_type','')}</strong><br>
                <span style="font-size:.84rem;">{r.get('description','')}</span><br>
                <span style="font-size:.8rem;color:{_SLATE};margin-top:4px;display:block;">
                    → {r.get('recommended_action','')}</span>
            </div>""", unsafe_allow_html=True)

    # ── Pricing & Seasonal ──
    st.markdown("""
    <div class="section-divider">
        <div class="section-divider-line"></div>
        <div class="section-divider-label">Market Intelligence</div>
        <div class="section-divider-line"></div>
    </div>""", unsafe_allow_html=True)
    p1, p2 = st.columns(2, gap="large")
    with p1:
        st.markdown('<div class="mini-label">💰 Pricing Sentiment</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="callout">{a.get("pricing_sentiment","")}</div>',
                    unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="mini-label">📅 Seasonal Patterns</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="callout">{a.get("seasonal_patterns","")}</div>',
                    unsafe_allow_html=True)


def _keyword_tags_html(keywords: list) -> str:
    """Inline chip version — still used in the report preview card."""
    colors = [
        ("EEF2FF", "4F46E5", "C7D2FE"),
        ("ECFEFF", "0891B2", "A5F3FC"),
        ("F0FDF4", "15803D", "BBF7D0"),
        ("FDF4FF", "9333EA", "E9D5FF"),
        ("FFF7ED", "C2410C", "FED7AA"),
    ]
    html = ""
    for i, kw in enumerate(keywords):
        bg, text, border = colors[i % len(colors)]
        html += (f'<span class="keyword-tag" style="background:#{bg};color:#{text};'
                 f'border:1px solid #{border}">🔑 {kw}</span>')
    return html


def _keyword_placement(kw: str) -> tuple[str, str, str, str, str]:
    """Return (label, bg_hex, text_hex, border_hex, where_to_use)."""
    kl = kw.lower()
    if any(w in kl for w in ["best", "top", "under $", "cheap", "affordable", "budget", "premium"]):
        return ("Title", "FEE2E2", "DC2626", "FECACA",
                "Add to your listing title for maximum visibility")
    if any(w in kl for w in ["for ", " for", "with ", " with", " that", "during", "when", "all day",
                               "all-day", "long", "extended", "daily", "everyday"]):
        return ("Bullet Point", "EEF2FF", "4F46E5", "C7D2FE",
                "Works well as a feature benefit in listing bullets")
    return ("Backend Search", "ECFDF5", "059669", "6EE7B7",
            "Add to Amazon backend search terms field")


def render_keyword_section(keywords: list, show_explainer: bool = True):
    """Renders the full functional keyword section with 2-col cards."""
    if not keywords:
        return

    if show_explainer:
        st.markdown("""
        <div class="kw-explainer">
            <div class="kw-explainer-title">🔑 What are Keyword Opportunities?</div>
            <div class="kw-explainer-body">
                These are exact phrases real customers use when searching for products like yours —
                extracted directly from their reviews. Adding these to your Amazon listing title,
                bullets, and backend search terms can significantly improve your search ranking
                and click-through rate.
            </div>
        </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    for i, kw in enumerate(keywords):
        label, badge_bg, badge_text, badge_border, where = _keyword_placement(kw)
        card_html = f"""
        <div class="kw-card">
            <div class="kw-card-top">
                <div class="kw-card-keyword">{kw}</div>
                <span class="kw-placement-badge"
                      style="background:#{badge_bg};color:#{badge_text};border:1px solid #{badge_border};">
                    📍 {label}
                </span>
                <div class="kw-where">{where}</div>
            </div>
            <div class="kw-card-bottom">
                <span class="kw-copy-hint">↓ click to copy</span>
            </div>
        </div>"""
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            st.markdown(card_html, unsafe_allow_html=True)
            st.code(kw, language=None)

    # Master copy block at the bottom
    st.markdown("""
    <div class="section-divider">
        <div class="section-divider-line"></div>
        <div class="section-divider-label">Copy All Keywords</div>
        <div class="section-divider-line"></div>
    </div>""", unsafe_allow_html=True)
    st.code(", ".join(keywords), language=None)


def tab_voc():
    if not st.session_state.analyzed:
        empty_state("🗣️", "No analysis yet",
                    "Run an analysis first to see Voice of Customer insights.")
        return

    a = st.session_state.analysis
    complaints = a.get("complaint_themes", [])
    praises    = a.get("praise_themes", [])
    kws        = a.get("keyword_opportunities", [])

    # ── VOC summary bar ──
    st.markdown(f"""
    <div class="voc-summary">
        <div class="voc-summary-item">
            <div class="voc-summary-number" style="color:#EF4444;">{len(complaints)}</div>
            <div class="voc-summary-label">Complaint Themes</div>
        </div>
        <div class="voc-summary-item">
            <div class="voc-summary-number" style="color:#10B981;">{len(praises)}</div>
            <div class="voc-summary-label">Praise Themes</div>
        </div>
        <div class="voc-summary-item">
            <div class="voc-summary-number" style="color:#4F46E5;">{len(kws)}</div>
            <div class="voc-summary-label">Keywords Found</div>
        </div>
    </div>""", unsafe_allow_html=True)

    # ── Complaints & Praise in 60/40 split ──
    left_col, right_col = st.columns([3, 2], gap="large")

    with left_col:
        st.markdown('<div class="section-title">🔴 Complaint Themes</div>', unsafe_allow_html=True)
        for t in complaints:
            intensity = t.get("emotional_intensity", "low")
            freq      = t.get("frequency_pct", 0)
            with st.expander(f"  {t['theme']}  ·  {freq}%  ·  {intensity.upper()}"):
                st.markdown(badge_html(intensity), unsafe_allow_html=True)
                st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
                st.markdown('<div class="mini-label">Frequency of Mention</div>', unsafe_allow_html=True)
                st.progress(int(freq))
                st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
                st.markdown('<div class="mini-label">Customer Quotes</div>', unsafe_allow_html=True)
                for q in t.get("example_quotes", [])[:2]:
                    st.markdown(f'<div class="quote-box">"{q}"</div>', unsafe_allow_html=True)
                st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
                st.markdown('<div class="mini-label">Improvement Recommendation</div>',
                            unsafe_allow_html=True)
                st.markdown(f'<div class="callout-green">{t.get("improvement_recommendation","")}</div>',
                            unsafe_allow_html=True)
                est = t.get("estimated_rating_impact", "")
                st.markdown(f"""
                <div style="background:#EEF2FF;border:1.5px solid #C7D2FE;border-radius:12px;
                             padding:14px;text-align:center;margin-top:10px;">
                    <div class="mini-label">Estimated Rating Impact</div>
                    <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1.7rem;
                                font-weight:800;color:{_INDIGO};margin-top:4px;">{est}</div>
                </div>""", unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="section-title">🟢 Praise Themes</div>', unsafe_allow_html=True)
        for t in praises:
            freq = t.get("frequency_pct", 0)
            with st.expander(f"  {t['theme']}  ·  {freq}%"):
                st.markdown('<div class="mini-label">Customer Quotes</div>', unsafe_allow_html=True)
                for q in t.get("example_quotes", [])[:2]:
                    st.markdown(f'<div class="quote-box">"{q}"</div>', unsafe_allow_html=True)
                st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
                st.progress(int(freq))
                st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
                st.markdown('<div class="mini-label">Marketing Angle</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="callout-green">{t.get("marketing_angle","")}</div>',
                            unsafe_allow_html=True)

    # ── Keywords ──
    st.markdown("""
    <div class="section-divider">
        <div class="section-divider-line"></div>
        <div class="section-divider-label">Keyword Opportunities</div>
        <div class="section-divider-line"></div>
    </div>""", unsafe_allow_html=True)
    render_keyword_section(kws, show_explainer=True)


def tab_personas():
    if not st.session_state.analyzed:
        empty_state("👥", "No analysis yet", "Run an analysis first to see Buyer Personas.")
        return

    a = st.session_state.analysis
    avatars = ["🎯", "💼", "🎧", "🏋️", "✈️", "📚", "🎁", "⚡"]
    persona_gradients = [
        "linear-gradient(145deg, #FFFFFF 0%, #EEF2FF 100%)",
        "linear-gradient(145deg, #FFFFFF 0%, #ECFEFF 100%)",
        "linear-gradient(145deg, #FFFFFF 0%, #F0FDF4 100%)",
        "linear-gradient(145deg, #FFFFFF 0%, #FDF4FF 100%)",
    ]
    accent_colors = [_INDIGO, _GREEN, _AMBER, "#8B5CF6"]

    for i, p in enumerate(a.get("buyer_personas", [])):
        emoji   = avatars[i % len(avatars)]
        pct     = p.get("percentage", "?")
        grad    = persona_gradients[i % len(persona_gradients)]
        accent  = accent_colors[i % len(accent_colors)]
        st.markdown(f"""
        <div class="persona-card" style="border-color:{accent}30;background:{grad};">
            <div style="display:flex;align-items:center;gap:16px;margin-bottom:14px;">
                <div style="font-size:2rem;background:white;border-radius:14px;border:1.5px solid {accent}30;
                            width:56px;height:56px;display:flex;align-items:center;justify-content:center;
                            box-shadow:0 2px 8px rgba(0,0,0,.06);">{emoji}</div>
                <div>
                    <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1.05rem;
                                font-weight:800;color:#0F172A;">{p.get('persona_name','')}</div>
                    <div style="font-size:.78rem;font-weight:600;color:{accent};margin-top:2px;">
                        Estimated {pct}% of buyers</div>
                </div>
            </div>
            <p style="color:{_SLATE};font-size:.875rem;margin:0;">{p.get('description','')}</p>
        </div>""", unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="medium")
        with c1:
            st.markdown('<div class="mini-label">💚 What They Love</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="callout-green">{p.get("what_they_love","")}</div>',
                        unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="mini-label">🔴 What Frustrates Them</div>',
                        unsafe_allow_html=True)
            st.markdown(f'<div class="callout-red">{p.get("what_frustrates_them","")}</div>',
                        unsafe_allow_html=True)
        st.markdown('<div class="mini-label">📣 Marketing Message</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:white;border:1.5px solid {accent}40;border-radius:12px;
                    padding:16px 20px;margin-bottom:8px;
                    box-shadow:0 1px 4px rgba(0,0,0,.04);">
            <span style="font-style:italic;color:{accent};font-size:.9rem;font-weight:500;">
                "{p.get('marketing_message','')}"</span>
        </div>""", unsafe_allow_html=True)
        st.markdown("---")


def tab_listing():
    if not st.session_state.analyzed:
        empty_state("✍️", "No analysis yet", "Run an analysis first to see Listing Optimization.")
        return

    a  = st.session_state.analysis
    pi = st.session_state.product_info
    bullets          = a.get("listing_bullets", [])
    suggested_title  = a.get("listing_title_suggestion", "")
    current_title    = pi.get("title", "")
    kws              = a.get("keyword_opportunities", [])

    # ── Fix #3: Title comparison ──
    st.markdown('<div class="section-title">Product Title Optimization</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="title-compare-container">
        <div class="title-box before">
            <div class="title-box-header">❌ Current Title</div>
            <div class="title-box-text">{current_title}</div>
        </div>
        <div class="title-box after">
            <div class="title-box-header">✅ AI-Optimized Title</div>
            <div class="title-box-text">{suggested_title}</div>
        </div>
    </div>""", unsafe_allow_html=True)

    # ── Fix #6: Section divider ──
    st.markdown("""
    <div class="section-divider">
        <div class="section-divider-line"></div>
        <div class="section-divider-label">AI-Generated Listing Copy</div>
        <div class="section-divider-line"></div>
    </div>""", unsafe_allow_html=True)

    # ── Fix #2: Premium bullet cards ──
    st.markdown('<div class="section-title">Optimized Listing Bullets</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{_MUTED};font-size:.82rem;margin-bottom:1.25rem;">'
                'Written from real customer voice. Each bullet targets a proven review theme.</p>',
                unsafe_allow_html=True)

    bullets_html = ""
    for i, bullet in enumerate(bullets, 1):
        parts   = bullet.split(" — ", 1)
        keyword = parts[0] if len(parts) > 1 else f"Bullet {i}"
        text    = parts[1] if len(parts) > 1 else parts[0]
        bullets_html += f"""
        <div class="listing-bullet">
            <div class="bullet-number-strip">{i}</div>
            <div class="bullet-content">
                <div class="bullet-keyword">{keyword}</div>
                <div class="bullet-text">{text}</div>
                <div class="bullet-copy-hint">Use this bullet in your Amazon listing →</div>
            </div>
        </div>"""
    st.markdown(bullets_html, unsafe_allow_html=True)

    # ── Fix #4: Download button ──
    st.markdown("<div style='height:.5rem;'></div>", unsafe_allow_html=True)
    full_copy = f"TITLE:\n{suggested_title}\n\nBULLETS:\n"
    for i, b in enumerate(bullets, 1):
        full_copy += f"{i}. {b}\n"
    st.download_button(
        label="📋  Download Full Listing Copy (.txt)",
        data=full_copy,
        file_name="revana_listing_copy.txt",
        mime="text/plain",
        use_container_width=True,
    )

    # ── Keyword opportunities ──
    st.markdown("""
    <div class="section-divider">
        <div class="section-divider-line"></div>
        <div class="section-divider-label">Keyword Opportunities</div>
        <div class="section-divider-line"></div>
    </div>""", unsafe_allow_html=True)
    render_keyword_section(kws, show_explainer=False)


def tab_trends():
    if not st.session_state.analyzed:
        empty_state("📈", "No analysis yet", "Run an analysis first to see Sentiment Trends.")
        return

    tr      = st.session_state.trends
    monthly = tr.get("monthly_data", [])
    direction = tr.get("trend_direction", "stable")
    magnitude = tr.get("trend_magnitude", 0.0)
    arrow = "↑" if direction == "improving" else ("↓" if direction == "declining" else "→")
    color = _GREEN if direction == "improving" else (_RED if direction == "declining" else _AMBER)
    bg_map = {_GREEN: "#ECFDF5", _RED: "#FEF2F2", _AMBER: "#FFFBEB"}
    bdr_map = {_GREEN: "#6EE7B7", _RED: "#FECACA", _AMBER: "#FCD34D"}

    # ── Summary strip ──
    s1, s2, s3, s4 = st.columns(4, gap="medium")
    s1.markdown(metric_card_html(arrow, "Trend Direction", direction.title(), "indigo"),
                unsafe_allow_html=True)
    s2.markdown(metric_card_html("📉" if direction == "declining" else "📈",
                                 "Magnitude", f"{magnitude:+.1f}%",
                                 "red" if direction == "declining" else "green"),
                unsafe_allow_html=True)
    s3.markdown(metric_card_html("📅", "Months Analyzed", str(len(monthly)), "cyan"),
                unsafe_allow_html=True)
    s4.markdown(metric_card_html("⚠️", "Spike Months",
                                 str(len(tr.get("spike_months", []))), "amber"),
                unsafe_allow_html=True)

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="callout" style="background:{bg_map.get(color,'#EEF2FF')};
                                border-left-color:{color};">
        {tr.get("insight","")}
    </div>""", unsafe_allow_html=True)

    if len(monthly) >= 2:
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        st.plotly_chart(chart_trends_line(monthly), use_container_width=True,
                        config={"displayModeBar": False})
        st.plotly_chart(chart_volume_bar(monthly, tr.get("spike_months", [])),
                        use_container_width=True, config={"displayModeBar": False})

        spikes = tr.get("spike_months", [])
        if spikes:
            st.markdown("---")
            st.markdown('<div class="section-title">⚠️ Complaint Spike Months</div>',
                        unsafe_allow_html=True)
            for m in spikes:
                md = next((x for x in monthly if x["month"] == m), {})
                st.markdown(f"""
                <div class="callout-red">
                    <strong style="color:#DC2626;">📍 {m}</strong>
                    &nbsp;—&nbsp; complaint rate: <strong>{md.get('complaint_rate',0):.1f}%</strong>
                    &nbsp;·&nbsp; {md.get('review_count',0)} reviews
                    &nbsp;·&nbsp; avg rating: {md.get('average_rating','N/A')}
                </div>""", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown('<div class="section-title">Monthly Breakdown</div>', unsafe_allow_html=True)
        table_df = pd.DataFrame([
            {"Month": m["month"], "Reviews": m["review_count"],
             "Avg Rating": m.get("average_rating"), "Complaint %": m.get("complaint_rate"),
             "Praise %": m.get("praise_rate"), "Verified %": m.get("verified_purchase_rate")}
            for m in monthly
        ])
        st.dataframe(table_df, use_container_width=True, hide_index=True)
    else:
        st.info("Not enough monthly data to render charts — at least 2 months of reviews needed.")


def tab_competitor():
    if not st.session_state.get("gap_analysis"):
        st.markdown("""
        <div style="text-align:center;padding:3rem 2rem;
                    background:white;border-radius:16px;
                    border:1px solid #E2E8F0;">
            <div style="font-size:2rem;margin-bottom:1rem">⚔️</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif;
                        font-size:1.1rem;font-weight:700;color:#0F172A;
                        margin-bottom:0.5rem">No Competitor Added</div>
            <div style="font-size:0.9rem;color:#64748B">
                Go to the Analyze tab and enter a competitor ASIN
                to unlock this section.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    comp    = st.session_state.competitor
    gap     = st.session_state.gap_analysis
    pi      = st.session_state.product_info
    comp_pi = comp["product_info"]

    # ── Header ──
    h1, h2 = st.columns(2, gap="large")
    with h1:
        st.markdown(f"""
        <div class="comp-card-mine">
            <div class="mini-label" style="color:{_INDIGO};">My Product</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:.95rem;
                        font-weight:700;color:#0F172A;margin:8px 0;">
                {pi.get('title','')[:70]}…</div>
            <span style="font-size:1.5rem;font-weight:800;color:{_INDIGO};">
                {pi.get('overall_rating')}/5</span>
            <span style="color:{_MUTED};font-size:.8rem;margin-left:8px;">
                {pi.get('total_reviews',0):,} reviews</span>
        </div>""", unsafe_allow_html=True)
    with h2:
        st.markdown(f"""
        <div class="comp-card-comp">
            <div class="mini-label" style="color:{_AMBER};">Competitor</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:.95rem;
                        font-weight:700;color:#0F172A;margin:8px 0;">
                {comp_pi.get('title','')[:70]}…</div>
            <span style="font-size:1.5rem;font-weight:800;color:{_AMBER};">
                {comp_pi.get('overall_rating')}/5</span>
            <span style="color:{_MUTED};font-size:.8rem;margin-left:8px;">
                {comp_pi.get('total_reviews',0):,} reviews</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # ── Charts ──
    scores = gap.get("head_to_head_scores", {})
    if scores:
        cc1, cc2 = st.columns([1, 1], gap="large")
        with cc1:
            st.plotly_chart(chart_head_to_head(scores, pi.get("title","Mine"),
                                               comp_pi.get("title","Comp")),
                            use_container_width=True, config={"displayModeBar": False})
        with cc2:
            st.plotly_chart(chart_scores_bar(scores, pi.get("title","Mine"),
                                             comp_pi.get("title","Comp")),
                            use_container_width=True, config={"displayModeBar": False})

    st.markdown("---")

    # ── Advantages & Vulnerabilities ──
    ac, vc = st.columns(2, gap="large")
    with ac:
        st.markdown('<div class="section-title">💚 My Advantages</div>', unsafe_allow_html=True)
        for item in gap.get("my_advantages", []):
            st.markdown(f"""
            <div class="adv-card">
                <div style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;
                            color:#065F46;margin-bottom:10px;">✓ {item.get('advantage','')}</div>
                <div class="quote-box" style="background:#F0FDF4;border-left-color:#10B981;
                                             color:#065F46;">"{item.get('evidence','')}"</div>
                <div style="margin-top:10px;font-size:.81rem;color:{_SLATE};">
                    📣 {item.get('marketing_angle','')}</div>
            </div>""", unsafe_allow_html=True)
    with vc:
        st.markdown('<div class="section-title">🔴 My Vulnerabilities</div>', unsafe_allow_html=True)
        for v in gap.get("my_vulnerabilities", []):
            st.markdown(f"""
            <div class="vuln-card">
                <div style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;
                            color:#7F1D1D;margin-bottom:10px;">✗ {v.get('vulnerability','')}</div>
                <div class="quote-box" style="background:#FFF1F2;border-left-color:#EF4444;
                                             color:#9F1239;">"{v.get('evidence','')}"</div>
                <div style="margin-top:10px;font-size:.81rem;color:{_SLATE};">
                    🔧 {v.get('fix_recommendation','')}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    op1, op2 = st.columns(2, gap="large")
    with op1:
        st.markdown('<div class="mini-label">🌍 Market Opportunity</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="callout">{gap.get("market_opportunity","")}</div>',
                    unsafe_allow_html=True)
    with op2:
        st.markdown('<div class="mini-label">🎯 Positioning Statement</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#EEF2FF,#F5F3FF);
                    border:1.5px solid #C7D2FE;border-radius:14px;padding:20px;
                    box-shadow:0 1px 4px rgba(79,70,229,.08);">
            <span style="font-style:italic;color:{_INDIGO};font-size:.95rem;
                         font-weight:600;line-height:1.7;">
                "{gap.get('positioning_statement','')}"</span>
        </div>""", unsafe_allow_html=True)


def tab_export():
    import json as _json
    if not st.session_state.analyzed:
        empty_state("📥", "No analysis yet", "Run an analysis first to enable exports.")
        return

    a   = st.session_state.analysis
    pi  = st.session_state.product_info
    fs  = st.session_state.filter_stats
    now = datetime.now().strftime("%B %d, %Y")
    asin = pi.get("asin", "—")
    score = a.get("overall_health_score", 0)
    score_color = health_color(score)

    complaints = a.get("complaint_themes", [])
    praises    = a.get("praise_themes", [])
    bullets    = a.get("listing_bullets", [])

    # ── Build complaint rows HTML ──
    complaint_rows = ""
    for i, t in enumerate(complaints[:5], 1):
        freq      = t.get("frequency_pct", 0)
        intensity = t.get("emotional_intensity", "low")
        rec       = t.get("improvement_recommendation", "")[:120]
        badge_col = {"critical": "#EF4444", "high": "#F97316",
                     "medium": "#F59E0B", "low": "#10B981"}.get(intensity.lower(), "#94A3B8")
        complaint_rows += f"""
        <div class="report-complaint-row">
            <div class="report-complaint-rank">{i}</div>
            <div style="flex:1;">
                <div class="report-complaint-theme">{t.get('theme','')}</div>
                <div class="report-complaint-meta">
                    {freq}% of reviews &nbsp;·&nbsp;
                    <span style="color:{badge_col};font-weight:600;">{intensity.upper()}</span>
                    &nbsp;·&nbsp; Impact: {t.get('estimated_rating_impact','—')}
                </div>
                <div class="report-complaint-rec">→ {rec}{'…' if len(t.get('improvement_recommendation',''))>120 else ''}</div>
            </div>
        </div>"""

    # ── Build praise rows HTML ──
    praise_rows = ""
    for i, t in enumerate(praises[:3], 1):
        freq = t.get("frequency_pct", 0)
        angle = t.get("marketing_angle", "")[:100]
        praise_rows += f"""
        <div class="report-complaint-row">
            <div class="report-complaint-rank praise">{i}</div>
            <div style="flex:1;">
                <div class="report-complaint-theme">{t.get('theme','')}</div>
                <div class="report-complaint-meta">{freq}% of reviews</div>
                <div class="report-complaint-rec">📣 {angle}{'…' if len(t.get('marketing_angle',''))>100 else ''}</div>
            </div>
        </div>"""

    # ── Build bullet preview HTML ──
    bullet_rows = ""
    for i, b in enumerate(bullets[:5], 1):
        short = b[:110] + ("…" if len(b) > 110 else "")
        bullet_rows += f"""
        <div class="report-bullet-preview">
            <span class="report-bullet-num">{i}</span>
            <span>{short}</span>
        </div>"""

    # ── Build keyword chips ──
    kw_chips = "".join(
        f'<span style="display:inline-block;background:#EEF2FF;color:#4F46E5;'
        f'border:1px solid #C7D2FE;border-radius:20px;padding:2px 10px;'
        f'font-size:.72rem;font-weight:600;margin:2px;">{k}</span>'
        for k in a.get("keyword_opportunities", [])[:8]
    )

    # ── Render the report preview card ──
    st.markdown(f"""
    <div class="report-preview">

      <!-- Header -->
      <div class="report-header">
        <div style="position:relative;z-index:1;">
          <div class="report-brand">Revana &nbsp;·&nbsp; Voice of Customer Brief</div>
          <div class="report-title">{pi.get('title','Product')[:72]}{'…' if len(pi.get('title',''))>72 else ''}</div>
          <div class="report-subtitle">AI-powered analysis by Claude · Anthropic</div>
          <div class="report-meta">
            <div class="report-meta-item">ASIN &nbsp;<span>{asin}</span></div>
            <div class="report-meta-item">Rating &nbsp;<span>{pi.get('overall_rating','—')}/5</span></div>
            <div class="report-meta-item">Reviews analysed &nbsp;<span>{fs.get('trusted_count',0)}</span></div>
            <div class="report-meta-item">Fake filtered &nbsp;<span>{fs.get('flagged_count',0)}</span></div>
            <div class="report-meta-item">Generated &nbsp;<span>{now}</span></div>
          </div>
        </div>
      </div>

      <!-- Body -->
      <div class="report-body">

        <!-- Health score strip -->
        <div style="display:flex;align-items:center;gap:1.5rem;background:#F8FAFC;
                    border-radius:12px;padding:1rem 1.25rem;margin-bottom:1.75rem;
                    border:1px solid #E2E8F0;">
          <div style="text-align:center;min-width:60px;">
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:2.5rem;
                        font-weight:900;color:{score_color};line-height:1;">{score}</div>
            <div style="font-size:.65rem;color:#94A3B8;text-transform:uppercase;
                        letter-spacing:.5px;font-weight:600;">Health Score</div>
          </div>
          <div style="width:1px;height:48px;background:#E2E8F0;"></div>
          <div style="flex:1;">
            <div style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;
                        color:{score_color};font-size:.95rem;">{health_label(score)}</div>
            <div style="font-size:.82rem;color:#64748B;margin-top:.2rem;line-height:1.5;">
              {a.get('executive_summary','')[:200]}{'…' if len(a.get('executive_summary',''))>200 else ''}
            </div>
          </div>
        </div>

        <!-- Executive Summary -->
        <div class="report-section">
          <div class="report-section-title">Executive Summary</div>
          <div class="report-summary-text">{a.get('executive_summary','')}</div>
        </div>

        <!-- Complaint Themes -->
        <div class="report-section">
          <div class="report-section-title">🔴 Top Complaint Themes</div>
          {complaint_rows}
        </div>

        <!-- Praise Themes -->
        <div class="report-section">
          <div class="report-section-title">🟢 Top Praise Themes</div>
          {praise_rows}
        </div>

        <!-- Listing Bullets -->
        <div class="report-section">
          <div class="report-section-title">✍️ AI-Optimized Listing Bullets</div>
          {bullet_rows}
        </div>

        <!-- Keywords -->
        <div class="report-section" style="margin-bottom:0;">
          <div class="report-section-title">🔑 Keyword Opportunities</div>
          <div style="margin-top:.25rem;">{kw_chips}</div>
        </div>

      </div><!-- /report-body -->

      <!-- Footer bar -->
      <div class="report-footer-bar">
        <div class="report-footer-brand">⚡ Revana Report</div>
        <div class="report-footer-meta">
          Powered by Claude AI &nbsp;·&nbsp; Anthropic &nbsp;·&nbsp; {now}
        </div>
      </div>

    </div><!-- /report-preview -->
    """, unsafe_allow_html=True)

    # ── Download options ──
    st.markdown("""
    <div class="section-divider" style="margin-top:2rem;">
        <div class="section-divider-line"></div>
        <div class="section-divider-label">Download Options</div>
        <div class="section-divider-line"></div>
    </div>""", unsafe_allow_html=True)

    trusted = st.session_state.trusted_reviews.copy()
    if "date" in trusted.columns:
        trusted["date"] = trusted["date"].apply(
            lambda x: x.get("utc", str(x)) if isinstance(x, dict) else str(x))
    buf = io.StringIO()
    trusted.to_csv(buf, index=False)

    e1, e2, e3 = st.columns(3, gap="large")
    with e1:
        st.markdown(f"""
        <div class="export-card" style="border-top:3px solid {_INDIGO};">
            <div class="export-icon">📄</div>
            <div class="export-title">Full Report</div>
            <div class="export-desc">Complete VoC brief — all themes, personas,<br>risk alerts, and recommendations</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        st.download_button("⬇️  Download (.txt)", build_text_report(),
                           file_name=f"revana_report_{asin}.txt",
                           mime="text/plain", use_container_width=True)
    with e2:
        st.markdown(f"""
        <div class="export-card" style="border-top:3px solid {_CYAN};">
            <div class="export-icon">📊</div>
            <div class="export-title">Reviews CSV</div>
            <div class="export-desc">All trusted reviews with trust scores,<br>ratings, dates, and verification status</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        st.download_button("⬇️  Download (.csv)", buf.getvalue(),
                           file_name=f"revana_reviews_{asin}.csv",
                           mime="text/csv", use_container_width=True)
    with e3:
        st.markdown(f"""
        <div class="export-card" style="border-top:3px solid {_GREEN};">
            <div class="export-icon">🔧</div>
            <div class="export-title">Analysis JSON</div>
            <div class="export-desc">Structured data for integration<br>into dashboards or other tools</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        st.download_button("⬇️  Download (.json)",
                           _json.dumps(a, indent=2),
                           file_name=f"revana_analysis_{asin}.json",
                           mime="application/json", use_container_width=True)


# ── Main ──────────────────────────────────────────────────────────────────
def main():
    defaults = {
        "analyzed": False,
        "product_info": {},
        "analysis": {},
        "trusted_reviews": None,
        "flagged_reviews": None,
        "filter_stats": {},
        "trends": {},
        "rating_distribution": {},
        "gap_analysis": None,
        "competitor_info": None,
        "competitor_analysis": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    # ── Gradient header ──
    st.markdown("""
    <div class="revana-header">
        <div style="position:relative;z-index:1;">
            <div class="revana-logo">Revana<span>.</span></div>
            <div class="revana-tagline">AI-Powered Review Intelligence for Amazon Sellers</div>
            <span class="revana-badge">✦ Powered by Claude AI</span>
        </div>
        <div class="revana-header-glow"></div>
    </div>""", unsafe_allow_html=True)

    # ── Tabs ──
    tabs = st.tabs([
        "🔍 Analyze", "📊 Overview", "🗣️ Voice of Customer",
        "👥 Buyer Personas", "✍️ Listing Optimizer",
        "📈 Trends", "⚔️ Competitor", "📥 Export",
    ])

    # ── Analyze ──
    with tabs[0]:
        if st.session_state.analyzed:
            pi = st.session_state.product_info
            st.success(f"✅ Active analysis: **{pi.get('title','')[:70]}**  "
                       f"(ASIN: {pi.get('asin')}) — explore the tabs above.")
            st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

        st.markdown('<div class="section-title">Analyze a Product</div>', unsafe_allow_html=True)

        with st.form("analyze_form"):
            demo_mode = st.checkbox(
                "⚡  Demo Mode  —  instant results with pre-loaded data, no API key needed",
                value=not bool(st.session_state.analyzed),
            )
            st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
            c1, c2 = st.columns(2, gap="large")
            with c1:
                asin = st.text_input("Amazon ASIN", placeholder="e.g. B07PXGQC1Q",
                        help="Find the ASIN in the Amazon product URL or under Product Details")
            with c2:
                comp_asin = st.text_input("Competitor ASIN (optional)", placeholder="e.g. B09JQL3NWT",
                        help="Enter a second ASIN to unlock the Competitor tab")
            st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("🚀  Run Analysis", use_container_width=False)

        if submitted:
            if not demo_mode and not asin.strip():
                st.error("Enter an ASIN or enable Demo Mode.")
            else:
                run_analysis(asin.strip() if not demo_mode else "DEMO001",
                             comp_asin.strip(), demo_mode)

        # ── How it works ──
        st.markdown("---")
        st.markdown('<div class="section-title">How Revana Works</div>', unsafe_allow_html=True)
        steps = [
            ("🔍", "Fetch",    "Pull live product data and reviews via Rainforest API"),
            ("🧹", "Filter",   "Remove fake reviews using 12 heuristic signals"),
            ("🤖", "Analyse",  "Claude AI reads every trusted review to extract patterns"),
            ("📋", "Brief",    "Get complaint themes, personas, risk alerts, and more"),
            ("⚔️", "Compete",  "Add a competitor ASIN for a full gap analysis"),
        ]
        cols = st.columns(5, gap="small")
        for col, (icon, title, body) in zip(cols, steps):
            col.markdown(f"""
            <div class="step-card">
                <div style="font-size:1.8rem;margin-bottom:10px;">{icon}</div>
                <div style="font-family:'Plus Jakarta Sans',sans-serif;color:#0F172A;
                            font-weight:700;font-size:.9rem;margin-bottom:6px;">{title}</div>
                <div style="color:{_MUTED};font-size:.76rem;line-height:1.45;">{body}</div>
            </div>""", unsafe_allow_html=True)

    with tabs[1]: tab_overview()
    with tabs[2]: tab_voc()
    with tabs[3]: tab_personas()
    with tabs[4]: tab_listing()
    with tabs[5]: tab_trends()
    with tabs[6]: tab_competitor()
    with tabs[7]: tab_export()

    st.markdown("""
    <div class="footer">
        <strong style="color:#475569;">Revana</strong>
        &nbsp;·&nbsp; AI-Powered Review Intelligence
        &nbsp;·&nbsp; <span class="powered-badge">✦ Claude AI by Anthropic</span>
    </div>""", unsafe_allow_html=True)


main()
