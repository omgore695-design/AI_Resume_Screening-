
# AI Resume Screening System
An AI-powered Resume Screening & Candidate Ranking System built using NLP, Machine Learning, and Streamlit.

#  Project Overview
This system automatically analyzes resumes and compares them with a Job Description (JD).
It helps recruiters:
- Screen resumes faster
- Rank candidates automatically
- Detect missing skills
- Improve hiring efficiency

 # Features
✅ Resume Parsing (PDF/DOCX)  
✅ NLP Text Preprocessing  
✅ Skill Extraction  
✅ Resume Matching  
✅ Cosine Similarity Scoring  
✅ Candidate Ranking  
✅ Missing Skill Detection  
✅ Attractive Streamlit Dashboard  
✅ AI-Powered Screening  

# Technologies Used
| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Streamlit | Web UI |
| Scikit-learn | ML & TF-IDF |
| NLTK | NLP Processing |
| Pandas | Data Handling |
| PDFPlumber | PDF Parsing |
| Sentence Transformers | Advanced Embeddings |

---

# 📂 Project Structure
AI_Resume_Screening/
│
├── data/
│   ├── resumes/
│   ├── job_descriptions/
│
├── src/
│   ├── parser.py
│   ├── preprocess.py
│   ├── matcher.py
│   ├── skill_extractor.py
│
├── app.py
├── requirements.txt
├── README.md

# Run Project
streamlit run app.py

#  How It Works
1. Upload Resume Files
2. Enter Job Description
3. System Extracts Resume Text
4. NLP Preprocessing
5. Skill Extraction
6. AI Similarity Matching
7. Resume Ranking

---

# 🖥️ Dashboard Preview

## 🔥 Main Dashboard

Add Screenshot Here
<img width="1882" height="906" alt="image" src="https://github.com/user-attachments/assets/f2755a30-e5cf-49e9-9fab-ae078813dcf3" />

# 📈 Output Example
| Resume | Match Score |
|---|---|
| resume1.pdf | 92% |
| resume2.pdf | 81% |
| resume3.pdf | 74% |

#  Future Improvements
- Resume Upload UI
- BERT Embeddings
- AI Chatbot
- PDF Report Generation
- ATS Score Calculation
- Cloud Deployment
- Recruiter Login System

### Why this project?
This project solves a real-world HR Tech problem using NLP and AI.

### How matching works?
The system uses TF-IDF / Sentence Transformers and Cosine Similarity to compare resumes with job descriptions.

### Why NLP?
NLP helps understand resume content semantically rather than simple keyword matching.

# Author
Om Gore

# ⭐ If you like this project, give it a star!
