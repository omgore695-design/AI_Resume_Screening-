import streamlit as st
import os
import pandas as pd

from src.parser import extract_text
from src.preprocess import preprocess_text
from src.matcher import match_resume
from src.skill_extractor import extract_skills

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Background */

.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

/* Main Title */

.main-title {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    background: linear-gradient(to right, #00F5A0, #00D9F5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

/* Subtitle */

.subtitle {
    text-align: center;
    color: #D3D3D3;
    font-size: 20px;
    margin-bottom: 40px;
}

/* Glass Card */

.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    margin-bottom: 20px;
}

/* Buttons */

.stButton>button {
    width: 100%;
    border-radius: 15px;
    height: 3.5em;
    border: none;
    font-size: 18px;
    font-weight: bold;
    color: white;
    background: linear-gradient(90deg, #00F5A0, #00D9F5);
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px rgba(0,255,255,0.5);
}

/* Text Area */

textarea {
    background-color: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 15px !important;
}

/* Metric Card */

.metric-card {
    background: rgba(255,255,255,0.07);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(0,255,255,0.1);
}

/* Resume Cards */

.resume-card {
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    border-left: 6px solid #00F5A0;
    box-shadow: 0px 0px 20px rgba(0,255,255,0.15);
}

/* Score */

.score {
    font-size: 32px;
    font-weight: bold;
    color: #00F5A0;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #111827;
}

/* Dataframe */

[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.05);
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🚀 AI Resume Screener")

    st.write("---")

    st.markdown("""
    ### 📌 Features
    
    ✅ Resume Parsing  
    ✅ AI Skill Matching  
    ✅ Resume Ranking  
    ✅ Missing Skills Detection  
    ✅ ATS Style Screening  
    """)

    st.write("---")

    st.info("Built using NLP + Machine Learning")

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="main-title">
AI Resume Screening System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Smart AI-Powered Candidate Ranking & Resume Analysis Platform
</div>
""", unsafe_allow_html=True)

# ---------------- JOB DESCRIPTION ---------------- #

st.markdown('<div class="glass">', unsafe_allow_html=True)

st.subheader("📄 Enter Job Description")

jd = st.text_area(
    "",
    height=220,
    placeholder="Paste Job Description Here..."
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ANALYZE BUTTON ---------------- #

if st.button("🚀 Analyze Resumes"):

    resume_folder = "data/resumes"

    results = []

    if jd.strip() == "":
        st.warning("Please enter Job Description")
    else:

        with st.spinner("Analyzing resumes using AI..."):

            for file in os.listdir(resume_folder):

                file_path = os.path.join(resume_folder, file)

                try:

                    # Extract Resume Text
                    text = extract_text(file_path)

                    # Preprocessing
                    cleaned_resume = preprocess_text(text)
                    cleaned_jd = preprocess_text(jd)

                    # Matching
                    score = match_resume(cleaned_resume, cleaned_jd)

                    # Skills
                    skills = extract_skills(text)

                    # JD Skills
                    jd_skills = extract_skills(jd)

                    # Missing Skills
                    missing_skills = list(set(jd_skills) - set(skills))

                    results.append({
                        "Resume": file,
                        "Match Score": score,
                        "Skills": ", ".join(skills),
                        "Missing Skills": ", ".join(missing_skills)
                    })

                except Exception as e:
                    st.error(f"Error processing {file}: {e}")

        # Sort
        results = sorted(results, key=lambda x: x["Match Score"], reverse=True)

        st.success("AI Analysis Completed Successfully ✅")

        st.write("")

        # ---------------- TOP METRICS ---------------- #

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="metric-card">
            <h2>{len(results)}</h2>
            <p>Total Resumes</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            top_score = results[0]["Match Score"]

            st.markdown(f"""
            <div class="metric-card">
            <h2>{top_score}%</h2>
            <p>Highest Match</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-card">
            <h2>AI</h2>
            <p>Powered Ranking</p>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.write("## 📊 Candidate Results")

        # ---------------- RESULT CARDS ---------------- #

        for result in results:

            st.markdown(f"""
            <div class="resume-card">

                <h2>📄 {result['Resume']}</h2>

                <div class="score">
                    {result['Match Score']}% Match
                </div>

                <br>

                <b>✅ Skills Found:</b><br>
                {result['Skills']}

                <br><br>

                <b>❌ Missing Skills:</b><br>
                {result['Missing Skills']}

            </div>
            """, unsafe_allow_html=True)

        # ---------------- TABLE ---------------- #

        st.write("## 🏆 Resume Ranking Table")

        df = pd.DataFrame(results)

        st.dataframe(df, use_container_width=True)