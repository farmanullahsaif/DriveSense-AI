import streamlit as st

from coordinator import vehicle_graph


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="DriveSense AI",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# SESSION STATE
# ============================================================

if "diagnosis_result" not in st.session_state:
    st.session_state.diagnosis_result = None


# ============================================================
# HELPERS
# ============================================================

def reset_app():
    st.session_state.diagnosis_result = None

    keys = [
        "vehicle_make",
        "vehicle_model",
        "vehicle_year",
        "vehicle_engine",
        "vehicle_mileage",
        "vehicle_warning",
        "vehicle_symptom",
        "vehicle_obd",
    ]

    for key in keys:
        st.session_state.pop(key, None)

    st.rerun()


# ============================================================
# PREMIUM DESIGN SYSTEM
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       DESIGN TOKENS
       ======================================================== */

    :root {
        --bg-0: #030711;
        --bg-1: #071120;
        --bg-2: #0a1628;

        --panel: rgba(11, 22, 39, 0.72);
        --panel-strong: rgba(12, 24, 43, 0.94);

        --white: #f7fbff;
        --text: #e9f2ff;
        --muted: #8494ab;

        --blue: #3b82f6;
        --blue-2: #60a5fa;
        --cyan: #22d3ee;
        --purple: #8b5cf6;

        --green: #22c55e;
        --amber: #f59e0b;
        --red: #ef4444;

        --light-panel: #f8fafc;
        --light-text: #172033;
        --light-muted: #64748b;
        --light-border: #dce4ee;
    }


    /* ========================================================
       APP BACKGROUND
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 8% 4%,
                rgba(59,130,246,0.16),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 7%,
                rgba(34,211,238,0.11),
                transparent 24%
            ),
            radial-gradient(
                circle at 50% 70%,
                rgba(139,92,246,0.055),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                var(--bg-0),
                var(--bg-1) 45%,
                #06101d 100%
            );

        color: var(--text);
    }


    /* ========================================================
       MAIN WIDTH
       ======================================================== */

    .block-container {
        max-width: 1240px;
        padding-top: 0.8rem;
        padding-bottom: 4.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }


    /* ========================================================
       HIDE UNNECESSARY STREAMLIT DECORATION
       ======================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ========================================================
       TOP NAV
       ======================================================== */

    .ds-nav {
        position: relative;

        display: flex;
        align-items: center;
        justify-content: space-between;

        gap: 1rem;

        padding: 0.65rem 0.85rem;
        margin-bottom: 1rem;

        border:
            1px solid
            rgba(255,255,255,0.085);

        border-radius: 15px;

        background:
            rgba(6, 14, 27, 0.72);

        backdrop-filter:
            blur(18px);

        box-shadow:
            0 10px 35px
            rgba(0,0,0,0.18);
    }

    .ds-nav-left {
        display: flex;
        align-items: center;
        gap: 0.55rem;

        color: #edf5ff;

        font-size: 0.86rem;
        font-weight: 800;
    }

    .ds-online {
        width: 8px;
        height: 8px;

        border-radius: 50%;

        background: var(--green);

        box-shadow:
            0 0 0 0
            rgba(34,197,94,0.55);

        animation:
            ds-pulse 1.8s infinite;
    }

    .ds-nav-muted {
        color: #78889f;

        font-size: 0.69rem;
        font-weight: 500;
    }

    .ds-nav-right {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        gap: 0.35rem;
    }

    .ds-nav-badge {
        padding: 0.25rem 0.55rem;

        border:
            1px solid
            rgba(255,255,255,0.07);

        border-radius: 999px;

        background:
            rgba(255,255,255,0.025);

        color: #aebbd0;

        font-size: 0.60rem;
        font-weight: 700;
        letter-spacing: 0.04em;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .ds-hero {
        position: relative;

        min-height: 495px;

        overflow: hidden;

        border:
            1px solid
            rgba(255,255,255,0.085);

        border-radius: 30px;

        background:
            linear-gradient(
                135deg,
                rgba(12,27,47,0.98),
                rgba(5,13,24,0.94)
            );

        box-shadow:
            0 35px 100px
            rgba(0,0,0,0.28);

        isolation: isolate;
    }


    /* ambient glow */

    .ds-hero-glow-a {
        position: absolute;

        width: 520px;
        height: 520px;

        top: -250px;
        right: -170px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(59,130,246,0.24),
                transparent 68%
            );

        filter: blur(2px);

        animation:
            ds-float-glow
            7s
            ease-in-out
            infinite
            alternate;
    }

    .ds-hero-glow-b {
        position: absolute;

        width: 420px;
        height: 420px;

        bottom: -260px;
        left: -150px;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(34,211,238,0.10),
                transparent 68%
            );

        animation:
            ds-float-glow
            10s
            ease-in-out
            infinite
            alternate-reverse;
    }


    /* animated grid */

    .ds-grid {
        position: absolute;
        inset: 0;

        opacity: 0.17;

        background-image:
            linear-gradient(
                rgba(255,255,255,0.055) 1px,
                transparent 1px
            ),
            linear-gradient(
                90deg,
                rgba(255,255,255,0.055) 1px,
                transparent 1px
            );

        background-size:
            44px 44px;

        mask-image:
            linear-gradient(
                to bottom,
                rgba(0,0,0,0.9),
                transparent 92%
            );

        animation:
            ds-grid-move
            18s
            linear
            infinite;
    }


    /* particles */

    .ds-particles span {
        position: absolute;

        width: 3px;
        height: 3px;

        border-radius: 50%;

        background: rgba(135,190,255,0.85);

        box-shadow:
            0 0 12px
            rgba(96,165,250,0.8);

        animation:
            ds-particle
            linear
            infinite;
    }

    .ds-p1 {
        left: 10%;
        top: 24%;
        animation-duration: 8s;
    }

    .ds-p2 {
        left: 28%;
        top: 72%;
        animation-duration: 11s;
        animation-delay: -3s;
    }

    .ds-p3 {
        left: 47%;
        top: 20%;
        animation-duration: 9s;
        animation-delay: -2s;
    }

    .ds-p4 {
        right: 31%;
        top: 60%;
        animation-duration: 12s;
        animation-delay: -6s;
    }

    .ds-p5 {
        right: 14%;
        top: 30%;
        animation-duration: 10s;
        animation-delay: -1s;
    }

    .ds-p6 {
        right: 8%;
        bottom: 20%;
        animation-duration: 13s;
        animation-delay: -5s;
    }


    /* hero layout */

    .ds-hero-content {
        position: relative;
        z-index: 5;

        display: grid;

        grid-template-columns:
            1.05fr
            0.95fr;

        align-items: center;

        gap: 2rem;

        min-height: 495px;

        padding: 2.15rem;
    }


    /* ========================================================
       HERO COPY
       ======================================================== */

    .ds-eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;

        padding:
            0.38rem
            0.72rem;

        border:
            1px solid
            rgba(96,165,250,0.21);

        border-radius:
            999px;

        background:
            rgba(59,130,246,0.08);

        color:
            #afd0ff;

        font-size:
            0.67rem;

        font-weight:
            800;

        text-transform:
            uppercase;

        letter-spacing:
            0.07em;
    }

    .ds-eyebrow-dot {
        width: 7px;
        height: 7px;

        border-radius: 50%;

        background:
            var(--green);

        animation:
            ds-pulse
            1.7s
            infinite;
    }


    .ds-headline {
        margin-top: 1.1rem;

        font-size:
            clamp(
                2.8rem,
                5vw,
                5rem
            );

        font-weight: 950;

        letter-spacing:
            -0.075em;

        line-height:
            0.92;

        color:
            #f5f9ff;
    }

    .ds-headline span {
        display: inline-block;

        background:
            linear-gradient(
                90deg,
                #72aaff,
                #38d5f4,
                #a0baff,
                #72aaff
            );

        background-size:
            240% 100%;

        -webkit-background-clip:
            text;

        -webkit-text-fill-color:
            transparent;

        animation:
            ds-gradient
            5s
            ease
            infinite;
    }


    .ds-description {
        max-width: 630px;

        margin-top: 1.15rem;

        color:
            #a8b8ce;

        font-size:
            0.96rem;

        line-height:
            1.72;
    }


    /* hero technology pills */

    .ds-tech-pills {
        display: flex;
        flex-wrap: wrap;

        gap: 0.45rem;

        margin-top: 1.25rem;
    }

    .ds-tech-pill {
        padding:
            0.42rem
            0.68rem;

        border:
            1px solid
            rgba(255,255,255,0.08);

        border-radius:
            999px;

        background:
            rgba(255,255,255,0.03);

        color:
            #bdc9da;

        font-size:
            0.68rem;
    }


    /* ========================================================
       DIAGNOSTIC CORE VISUAL
       ======================================================== */

    .ds-core {
        position: relative;

        display: flex;
        align-items: center;
        justify-content: center;

        min-height:
            340px;
    }


    .ds-core-outer {
        position: absolute;

        width: 305px;
        height: 305px;

        border-radius: 50%;

        border:
            1px solid
            rgba(96,165,250,0.19);

        box-shadow:
            0 0 80px
            rgba(59,130,246,0.08);

        animation:
            ds-rotate
            20s
            linear
            infinite;
    }

    .ds-core-outer::before,
    .ds-core-outer::after {
        content: "";

        position: absolute;

        inset: 18px;

        border-radius: 50%;

        border:
            1px dashed
            rgba(34,211,238,0.17);
    }

    .ds-core-outer::after {
        inset: 44px;

        border:
            1px solid
            rgba(139,92,246,0.12);
    }


    .ds-core-inner {
        position: relative;

        width: 205px;
        height: 205px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 50%;

        background:
            radial-gradient(
                circle,
                rgba(22,40,67,0.94),
                rgba(5,12,22,0.97)
            );

        border:
            1px solid
            rgba(255,255,255,0.08);

        box-shadow:
            inset 0 0 50px
            rgba(59,130,246,0.11),

            0 25px 70px
            rgba(0,0,0,0.28);
    }


    .ds-core-ring {
        position: absolute;

        inset: 17px;

        border-radius: 50%;

        border:
            2px solid
            transparent;

        border-top-color:
            #4f8cff;

        border-right-color:
            rgba(34,211,238,0.8);

        animation:
            ds-rotate
            4s
            linear
            infinite;
    }


    .ds-car {
        position: relative;
        z-index: 5;

        font-size:
            5.6rem;

        filter:
            drop-shadow(
                0 15px
                30px
                rgba(59,130,246,0.3)
            );

        animation:
            ds-car-float
            3.1s
            ease-in-out
            infinite;
    }


    .ds-scan {
        position: absolute;

        width: 235px;
        height: 2px;

        background:
            linear-gradient(
                90deg,
                transparent,
                #22d3ee,
                transparent
            );

        box-shadow:
            0 0 18px
            rgba(34,211,238,0.9);

        animation:
            ds-scan
            3.3s
            ease-in-out
            infinite;
    }


    .ds-core-label {
        position: absolute;

        bottom: -4px;

        padding:
            0.42rem
            0.72rem;

        border:
            1px solid
            rgba(255,255,255,0.07);

        border-radius:
            999px;

        color:
            #96a9c3;

        background:
            rgba(5,13,23,0.80);

        backdrop-filter:
            blur(12px);

        font-size:
            0.64rem;

        letter-spacing:
            0.04em;

        animation:
            ds-label-glow
            3s
            ease-in-out
            infinite;
    }


    /* ========================================================
       ENGINE PIPELINE
       ======================================================== */

    .ds-pipeline {
        display: flex;
        align-items: center;
        gap: 0;

        margin-top:
            1rem;

        overflow-x:
            auto;

        padding:
            0.1rem 0.1rem 0.7rem 0.1rem;
    }

    .ds-pipeline-step {
        flex:
            1 0 130px;

        min-width:
            130px;

        padding:
            0.85rem;

        border:
            1px solid
            rgba(255,255,255,0.075);

        border-radius:
            15px;

        background:
            rgba(255,255,255,0.028);

        transition:
            transform
            0.22s ease,
            border-color
            0.22s ease;
    }

    .ds-pipeline-step:hover {
        transform:
            translateY(-4px);

        border-color:
            rgba(96,165,250,0.30);
    }

    .ds-pipeline-icon {
        font-size:
            1.15rem;
    }

    .ds-pipeline-title {
        margin-top:
            0.35rem;

        color:
            #ecf4ff;

        font-size:
            0.73rem;

        font-weight:
            800;
    }

    .ds-pipeline-text {
        margin-top:
            0.2rem;

        color:
            #8190a7;

        font-size:
            0.62rem;

        line-height:
            1.4;
    }

    .ds-pipeline-arrow {
        flex:
            0 0 auto;

        color:
            #4c6a8d;

        padding:
            0 0.35rem;

        font-size:
            0.9rem;
    }


    /* ========================================================
       SECTION TITLE
       ======================================================== */

    .ds-section-title {
        margin-top:
            1.8rem;

        color:
            #f1f6ff;

        font-size:
            1.28rem;

        font-weight:
            900;

        letter-spacing:
            -0.03em;
    }

    .ds-section-subtitle {
        margin-top:
            0.22rem;

        color:
            #7d8da5;

        font-size:
            0.77rem;
    }


    /* ========================================================
       FORM AREA
       ======================================================== */

    .ds-form-intro {
        margin-bottom:
            0.9rem;

        color:
            #4b586e;

        font-size:
            0.78rem;
    }


    /* Force native form area to light theme */

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius:
            21px !important;
    }


    [data-testid="stVerticalBlockBorderWrapper"] .stMarkdown,
    [data-testid="stVerticalBlockBorderWrapper"] label,
    [data-testid="stVerticalBlockBorderWrapper"] p {
        color:
            #172033 !important;
    }


    [data-testid="stVerticalBlockBorderWrapper"] {
        background:
            #f8fafc !important;

        border:
            1px solid
            #dce4ee !important;

        box-shadow:
            0 20px 60px
            rgba(0,0,0,0.14);
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea {
        color:
            #162033 !important;

        background:
            #ffffff !important;

        border:
            1px solid
            #cbd5e1 !important;

        border-radius:
            11px !important;

        caret-color:
            #2563eb !important;
    }


    .stTextInput input:focus,
    .stNumberInput input:focus,
    .stTextArea textarea:focus {
        color:
            #162033 !important;

        background:
            #ffffff !important;

        border-color:
            #3b82f6 !important;

        box-shadow:
            0 0 0 3px
            rgba(59,130,246,0.12) !important;
    }


    input::placeholder,
    textarea::placeholder {
        color:
            #8b96a8 !important;

        opacity:
            1 !important;
    }


    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] label {
        color:
            #263248 !important;

        font-weight:
            750 !important;
    }


    /* selectbox */

    div[data-baseweb="select"] > div {
        background:
            #ffffff !important;

        border:
            1px solid
            #cbd5e1 !important;

        border-radius:
            11px !important;
    }

    div[data-baseweb="select"] * {
        color:
            #162033 !important;
    }


    /* number buttons */

    .stNumberInput button {
        color:
            #334155 !important;

        background:
            #f1f5f9 !important;

        border-color:
            #cbd5e1 !important;
    }


    /* ========================================================
       PRIMARY BUTTON
       ======================================================== */

    .stButton > button {
        min-height:
            3.35rem;

        border-radius:
            13px;

        font-weight:
            850;

        font-size:
            0.92rem;

        letter-spacing:
            0.01em;

        transition:
            transform
            0.18s ease,
            box-shadow
            0.18s ease;
    }

    .stButton > button:hover {
        transform:
            translateY(-2px);

        box-shadow:
            0 14px 34px
            rgba(59,130,246,0.21);
    }


    /* ========================================================
       RESULT PANELS
       ======================================================== */

    .ds-result-header {
        margin-top:
            1.6rem;

        padding:
            0.15rem 0;
    }

    .ds-result-title {
        color:
            #f4f8ff;

        font-size:
            1.45rem;

        font-weight:
            900;

        letter-spacing:
            -0.035em;
    }

    .ds-result-subtitle {
        margin-top:
            0.2rem;

        color:
            #7d8da5;

        font-size:
            0.76rem;
    }


    .ds-result-card {
        margin-top:
            0.85rem;

        border:
            1px solid
            rgba(255,255,255,0.075);

        border-radius:
            19px;

        padding:
            1rem 1.05rem;

        background:
            linear-gradient(
                180deg,
                rgba(14,27,47,0.88),
                rgba(8,17,30,0.89)
            );

        box-shadow:
            0 16px
            45px
            rgba(0,0,0,0.16);

        animation:
            ds-card-enter
            0.5s
            ease both;
    }


    .ds-card-kicker {
        color:
            #68a5ff;

        font-size:
            0.67rem;

        font-weight:
            800;

        text-transform:
            uppercase;

        letter-spacing:
            0.08em;
    }


    .ds-card-title {
        margin-top:
            0.25rem;

        color:
            #edf4ff;

        font-size:
            1rem;

        font-weight:
            850;
    }


    /* ========================================================
       METRICS
       ======================================================== */

    [data-testid="stMetric"] {
        border:
            1px solid
            rgba(255,255,255,0.075);

        border-radius:
            15px;

        padding:
            0.72rem;

        background:
            rgba(255,255,255,0.025);
    }

    [data-testid="stMetricLabel"] {
        color:
            #8090a8 !important;
    }

    [data-testid="stMetricValue"] {
        color:
            #f1f6ff !important;
    }


    /* ========================================================
       EXPANDERS
       ======================================================== */

    [data-testid="stExpander"] {
        border:
            1px solid
            rgba(255,255,255,0.08) !important;

        border-radius:
            15px !important;

        background:
            rgba(255,255,255,0.02) !important;
    }

    [data-testid="stExpander"] summary {
        color:
            #edf4ff !important;

        font-weight:
            750 !important;
    }


    /* result markdown */

    [data-testid="stExpander"] p,
    [data-testid="stExpander"] li,
    [data-testid="stExpander"] h1,
    [data-testid="stExpander"] h2,
    [data-testid="stExpander"] h3,
    [data-testid="stExpander"] strong {
        color:
            #dce7f7 !important;
    }


    /* ========================================================
       STATUS
       ======================================================== */

    [data-testid="stStatus"] {
        border-radius:
            16px !important;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .ds-footer {
        margin-top:
            2rem;

        padding:
            1.7rem
            0
            0.6rem;

        text-align:
            center;

        color:
            #627087;

        font-size:
            0.68rem;

        line-height:
            1.7;
    }


    /* ========================================================
       ANIMATIONS
       ======================================================== */

    @keyframes ds-pulse {

        0% {
            box-shadow:
                0 0 0 0
                rgba(34,197,94,0.55);
        }

        70% {
            box-shadow:
                0 0 0 9px
                rgba(34,197,94,0);
        }

        100% {
            box-shadow:
                0 0 0 0
                rgba(34,197,94,0);
        }
    }


    @keyframes ds-float-glow {

        0% {
            transform:
                translate3d(0,0,0)
                scale(1);
        }

        100% {
            transform:
                translate3d(-30px,25px,0)
                scale(1.12);
        }
    }


    @keyframes ds-grid-move {

        0% {
            background-position:
                0 0,
                0 0;
        }

        100% {
            background-position:
                44px 44px,
                44px 44px;
        }
    }


    @keyframes ds-particle {

        0% {
            transform:
                translateY(25px)
                translateX(0);

            opacity:
                0;
        }

        18% {
            opacity:
                1;
        }

        55% {
            opacity:
                0.9;
        }

        100% {
            transform:
                translateY(-145px)
                translateX(28px);

            opacity:
                0;
        }
    }


    @keyframes ds-gradient {

        0%, 100% {
            background-position:
                0% 50%;
        }

        50% {
            background-position:
                100% 50%;
        }
    }


    @keyframes ds-rotate {

        from {
            transform:
                rotate(0deg);
        }

        to {
            transform:
                rotate(360deg);
        }
    }


    @keyframes ds-car-float {

        0%, 100% {
            transform:
                translateY(0)
                rotate(-1deg);
        }

        50% {
            transform:
                translateY(-11px)
                rotate(1deg);
        }
    }


    @keyframes ds-scan {

        0% {
            transform:
                translateY(-105px);

            opacity:
                0;
        }

        18% {
            opacity:
                1;
        }

        50% {
            transform:
                translateY(105px);

            opacity:
                1;
        }

        85% {
            opacity:
                0.7;
        }

        100% {
            transform:
                translateY(-105px);

            opacity:
                0;
        }
    }


    @keyframes ds-label-glow {

        0%, 100% {
            box-shadow:
                0 0 0
                rgba(59,130,246,0);
        }

        50% {
            box-shadow:
                0 0 20px
                rgba(59,130,246,0.10);
        }
    }


    @keyframes ds-card-enter {

        from {
            opacity:
                0;

            transform:
                translateY(12px);
        }

        to {
            opacity:
                1;

            transform:
                translateY(0);
        }
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 1000px) {

        .ds-hero-content {
            grid-template-columns:
                1fr;

            min-height:
                auto;
        }

        .ds-core {
            min-height:
                265px;
        }

        .ds-hero {
            min-height:
                auto;
        }
    }


    @media (max-width: 650px) {

        .block-container {
            padding-left:
                0.55rem;

            padding-right:
                0.55rem;

            padding-top:
                0.35rem;
        }


        .ds-nav {
            flex-direction:
                column;

            align-items:
                flex-start;
        }


        .ds-nav-right {
            justify-content:
                flex-start;
        }


        .ds-hero {
            border-radius:
                22px;
        }


        .ds-hero-content {
            padding:
                1rem;
        }


        .ds-headline {
            font-size:
                2.65rem;
        }


        .ds-description {
            font-size:
                0.86rem;
        }


        .ds-core-outer {
            width:
                230px;

            height:
                230px;
        }


        .ds-core-inner {
            width:
                165px;

            height:
                165px;
        }


        .ds-car {
            font-size:
                4.5rem;
        }


        .ds-scan {
            width:
                185px;
        }


        .ds-pipeline {
            margin-right:
                -0.2rem;
        }


        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius:
                17px !important;
        }
    }

    </style>
    """
)


# ============================================================
# TOP NAVIGATION
# ============================================================

st.html(
    """
    <div class="ds-nav">

        <div class="ds-nav-left">

            <span class="ds-online"></span>

            <span>
                DriveSense AI
            </span>

            <span class="ds-nav-muted">
                Vehicle Intelligence Platform
            </span>

        </div>

        <div class="ds-nav-right">

            <span class="ds-nav-badge">MULTI-AGENT</span>
            <span class="ds-nav-badge">RAG</span>
            <span class="ds-nav-badge">OBD-II</span>
            <span class="ds-nav-badge">SAFETY-FIRST</span>

        </div>

    </div>
    """
)


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="ds-hero">

        <div class="ds-hero-glow-a"></div>
        <div class="ds-hero-glow-b"></div>

        <div class="ds-grid"></div>

        <div class="ds-particles">
            <span class="ds-p1"></span>
            <span class="ds-p2"></span>
            <span class="ds-p3"></span>
            <span class="ds-p4"></span>
            <span class="ds-p5"></span>
            <span class="ds-p6"></span>
        </div>


        <div class="ds-hero-content">

            <div>

                <div class="ds-eyebrow">
                    <span class="ds-eyebrow-dot"></span>
                    AI DIAGNOSTIC ENGINE ONLINE
                </div>


                <div class="ds-headline">
                    Your car speaks.<br>
                    <span>DriveSense listens.</span>
                </div>


                <div class="ds-description">
                    An intelligent vehicle diagnosis system that
                    understands symptoms, retrieves automotive
                    knowledge, interprets OBD-II information,
                    coordinates specialized AI agents, and
                    evaluates safety considerations.
                </div>


                <div class="ds-tech-pills">

                    <div class="ds-tech-pill">
                        🧠 Symptom Intelligence
                    </div>

                    <div class="ds-tech-pill">
                        📚 Automotive RAG
                    </div>

                    <div class="ds-tech-pill">
                        📟 OBD-II
                    </div>

                    <div class="ds-tech-pill">
                        🛡️ Safety Engine
                    </div>

                </div>

            </div>


            <div class="ds-core">

                <div class="ds-core-outer"></div>

                <div class="ds-core-inner">

                    <div class="ds-core-ring"></div>

                    <div class="ds-car">
                        🚙
                    </div>

                    <div class="ds-scan"></div>

                </div>

                <div class="ds-core-label">
                    SYSTEM READY • AWAITING VEHICLE DATA
                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# AI PIPELINE
# ============================================================

st.html(
    """
    <div class="ds-pipeline">

        <div class="ds-pipeline-step">
            <div class="ds-pipeline-icon">🧠</div>
            <div class="ds-pipeline-title">
                Symptoms
            </div>
            <div class="ds-pipeline-text">
                Understand user language.
            </div>
        </div>

        <div class="ds-pipeline-arrow">→</div>

        <div class="ds-pipeline-step">
            <div class="ds-pipeline-icon">📟</div>
            <div class="ds-pipeline-title">
                OBD-II
            </div>
            <div class="ds-pipeline-text">
                Analyze diagnostic codes.
            </div>
        </div>

        <div class="ds-pipeline-arrow">→</div>

        <div class="ds-pipeline-step">
            <div class="ds-pipeline-icon">📚</div>
            <div class="ds-pipeline-title">
                RAG
            </div>
            <div class="ds-pipeline-text">
                Retrieve relevant knowledge.
            </div>
        </div>

        <div class="ds-pipeline-arrow">→</div>

        <div class="ds-pipeline-step">
            <div class="ds-pipeline-icon">🔍</div>
            <div class="ds-pipeline-title">
                Diagnosis
            </div>
            <div class="ds-pipeline-text">
                Build possible causes.
            </div>
        </div>

        <div class="ds-pipeline-arrow">→</div>

        <div class="ds-pipeline-step">
            <div class="ds-pipeline-icon">🛡️</div>
            <div class="ds-pipeline-title">
                Safety
            </div>
            <div class="ds-pipeline-text">
                Evaluate risk.
            </div>
        </div>

        <div class="ds-pipeline-arrow">→</div>

        <div class="ds-pipeline-step">
            <div class="ds-pipeline-icon">📋</div>
            <div class="ds-pipeline-title">
                Report
            </div>
            <div class="ds-pipeline-text">
                Explain the next step.
            </div>
        </div>

    </div>
    """
)


# ============================================================
# SECTION TITLE
# ============================================================

st.html(
    """
    <div class="ds-section-title">
        Start a Vehicle Diagnosis
    </div>

    <div class="ds-section-subtitle">
        Provide enough context for the diagnostic engine to reason
        about your vehicle.
    </div>
    """
)


# ============================================================
# FORM CONTAINER
# ============================================================

with st.container(border=True):

    st.markdown(
        """
        <div style="
            color:#172033;
            font-size:1.18rem;
            font-weight:850;
            margin-bottom:0.2rem;">
            🚘 Vehicle Profile
        </div>

        <div style="
            color:#64748b;
            font-size:0.78rem;
            margin-bottom:1rem;">
            Basic vehicle details improve diagnostic context.
        </div>
        """,
        unsafe_allow_html=True,
    )


    col1, col2 = st.columns(2)


    with col1:

        make = st.text_input(
            "Vehicle Make",
            placeholder="Toyota",
            key="vehicle_make",
        )

        year = st.number_input(
            "Model Year",
            min_value=1950,
            max_value=2035,
            value=2020,
            step=1,
            key="vehicle_year",
        )

        mileage = st.number_input(
            "Mileage (km)",
            min_value=0,
            max_value=2_000_000,
            value=100_000,
            step=1_000,
            key="vehicle_mileage",
        )


    with col2:

        model = st.text_input(
            "Vehicle Model",
            placeholder="Corolla",
            key="vehicle_model",
        )

        engine = st.text_input(
            "Engine",
            placeholder="1.6L Petrol",
            key="vehicle_engine",
        )

        warning_light = st.selectbox(
            "Check Engine Light",
            [
                "Not sure",
                "No",
                "Yes - Steady",
                "Yes - Flashing",
            ],
            key="vehicle_warning",
        )


    st.markdown(
        """
        <div style="
            color:#172033;
            font-size:1.18rem;
            font-weight:850;
            margin-top:1.25rem;
            margin-bottom:0.2rem;">
            🔧 Describe the Problem
        </div>

        <div style="
            color:#64748b;
            font-size:0.78rem;
            margin-bottom:0.8rem;">
            Describe what the vehicle is doing in your own words.
        </div>
        """,
        unsafe_allow_html=True,
    )


    symptom = st.text_area(
        "Vehicle symptoms",
        placeholder=(
            "Example:\n"
            "My car jerks during acceleration, especially "
            "when starting from a stop. Sometimes it loses power."
        ),
        height=155,
        key="vehicle_symptom",
    )


    st.markdown(
        """
        <div style="
            color:#172033;
            font-size:1.18rem;
            font-weight:850;
            margin-top:1.25rem;
            margin-bottom:0.2rem;">
            📟 OBD-II Diagnostics
        </div>

        <div style="
            color:#64748b;
            font-size:0.78rem;
            margin-bottom:0.8rem;">
            Optional. Add diagnostic trouble codes if you have them.
        </div>
        """,
        unsafe_allow_html=True,
    )


    obd_codes = st.text_input(
        "OBD-II code(s)",
        placeholder="P0301, P0171",
        key="vehicle_obd",
    )


    st.caption(
        "No scanner? Leave this empty — DriveSense AI can still analyze symptoms."
    )


    st.write("")


    diagnose_clicked = st.button(
        "🚀  START AI DIAGNOSIS",
        type="primary",
        use_container_width=True,
    )


# ============================================================
# RUN DIAGNOSIS
# ============================================================

if diagnose_clicked:

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not make.strip():
        st.error("Please enter the vehicle make.")
        st.stop()

    if not model.strip():
        st.error("Please enter the vehicle model.")
        st.stop()

    if not engine.strip():
        st.error("Please enter the engine information.")
        st.stop()

    if not symptom.strip():
        st.error("Please describe the vehicle problem.")
        st.stop()


    # --------------------------------------------------------
    # STATE
    # --------------------------------------------------------

    initial_state = {
        "make": make.strip(),
        "model": model.strip(),
        "year": int(year),
        "engine": engine.strip(),
        "mileage": int(mileage),
        "symptom": symptom.strip(),
        "warning_light": warning_light,
        "obd_codes": obd_codes.strip(),
    }


    # --------------------------------------------------------
    # AI EXECUTION
    # --------------------------------------------------------

    with st.status(
        "DriveSense AI is running the diagnostic pipeline...",
        expanded=True,
    ) as status:

        st.write("🧠 Classifying vehicle symptoms...")
        st.write("📟 Processing OBD-II information...")
        st.write("📚 Retrieving relevant automotive knowledge...")
        st.write("🔍 Running diagnostic reasoning...")
        st.write("🛡️ Evaluating safety considerations...")
        st.write("📋 Generating vehicle report...")

        try:

            result = vehicle_graph.invoke(
                initial_state
            )

            status.update(
                label="✅ Diagnostic pipeline complete",
                state="complete",
                expanded=False,
            )

        except Exception as exc:

            status.update(
                label="❌ Diagnostic pipeline failed",
                state="error",
                expanded=True,
            )

            st.error(
                "DriveSense AI could not complete the analysis."
            )

            st.exception(exc)

            st.stop()


    st.session_state.diagnosis_result = result


# ============================================================
# RESULT DISPLAY
# ============================================================

result = st.session_state.diagnosis_result


if result:

    st.html(
        """
        <div class="ds-result-header">

            <div class="ds-result-title">
                Diagnostic Intelligence
            </div>

            <div class="ds-result-subtitle">
                Multi-agent analysis generated from the supplied
                vehicle information, symptoms, OBD-II data, and
                automotive knowledge.
            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # VEHICLE SNAPSHOT
    # --------------------------------------------------------

    m1, m2, m3, m4 = st.columns(4)


    with m1:

        st.metric(
            "Vehicle",
            f"{result.get('make', make)} "
            f"{result.get('model', model)}",
        )


    with m2:

        st.metric(
            "Model Year",
            str(
                result.get(
                    "year",
                    year,
                )
            ),
        )


    with m3:

        mileage_value = result.get(
            "mileage",
            mileage,
        )

        st.metric(
            "Mileage",
            f"{int(mileage_value):,} km",
        )


    with m4:

        st.metric(
            "OBD-II",
            "Provided"
            if obd_codes.strip()
            else "Not provided",
        )


    # --------------------------------------------------------
    # SYMPTOM
    # --------------------------------------------------------

    with st.container():

        st.html(
            """
            <div class="ds-result-card">

                <div class="ds-card-kicker">
                    SYMPTOM ENGINE
                </div>

                <div class="ds-card-title">
                    🧠 Symptom Intelligence
                </div>

            </div>
            """
        )

        text = result.get(
            "symptom_analysis"
        )

        if text:

            st.markdown(text)

        else:

            st.info(
                "No symptom analysis was returned."
            )


    # --------------------------------------------------------
    # OBD
    # --------------------------------------------------------

    with st.container():

        st.html(
            """
            <div class="ds-result-card">

                <div class="ds-card-kicker">
                    DIAGNOSTIC DATA
                </div>

                <div class="ds-card-title">
                    📟 OBD-II Intelligence
                </div>

            </div>
            """
        )

        text = result.get(
            "obd_analysis"
        )

        if obd_codes.strip() and text:

            st.markdown(text)

        else:

            st.info(
                "No OBD-II code was supplied."
            )


    # --------------------------------------------------------
    # DIAGNOSIS
    # --------------------------------------------------------

    with st.container():

        st.html(
            """
            <div class="ds-result-card">

                <div class="ds-card-kicker">
                    AI REASONING
                </div>

                <div class="ds-card-title">
                    🔍 Diagnostic Analysis
                </div>

            </div>
            """
        )

        text = result.get(
            "diagnosis"
        )

        if text:

            st.markdown(text)

        else:

            st.info(
                "No diagnostic analysis was returned."
            )


    # --------------------------------------------------------
    # SAFETY
    # --------------------------------------------------------

    st.html(
        """
        <div class="ds-section-title">
            🛡️ Safety Assessment
        </div>

        <div class="ds-section-subtitle">
            Safety is evaluated conservatively because DriveSense
            cannot physically inspect the vehicle.
        </div>
        """
    )


    with st.container():

        st.warning(
            "If the vehicle has severe braking or steering problems, "
            "overheating, smoke, fuel leakage, major loss of power, "
            "or another potentially dangerous symptom, arrange "
            "professional assistance rather than relying on AI guidance."
        )

        safety_text = result.get(
            "safety_assessment"
        )

        if safety_text:

            st.markdown(
                safety_text
            )

        else:

            st.info(
                "No safety assessment was returned."
            )


    # --------------------------------------------------------
    # FINAL REPORT
    # --------------------------------------------------------

    with st.container():

        st.html(
            """
            <div class="ds-result-card">

                <div class="ds-card-kicker">
                    VEHICLE REPORT
                </div>

                <div class="ds-card-title">
                    📋 DriveSense AI Summary
                </div>

            </div>
            """
        )

        final_report = result.get(
            "final_report"
        )

        if final_report:

            st.markdown(
                final_report
            )

        else:

            st.info(
                "No final report was returned."
            )


    # --------------------------------------------------------
    # NEW DIAGNOSIS
    # --------------------------------------------------------

    st.write("")

    if st.button(
        "🔄  START ANOTHER DIAGNOSIS",
        use_container_width=True,
    ):

        reset_app()


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="ds-footer">

        <strong>DriveSense AI</strong><br>

        Intelligent Vehicle Diagnosis System<br><br>

        Multi-Agent AI • Automotive RAG • OBD-II Analysis
        • Safety Assessment<br><br>

        DriveSense AI provides informational guidance and does not
        replace a qualified automotive technician. AI-generated
        information may be incomplete or incorrect. For safety-critical
        vehicle problems, seek professional assistance.

    </div>
    """
)