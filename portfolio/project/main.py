# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import zipfile
# from pypdf import PdfReader
# from langchain_core.messages import SystemMessage, HumanMessage
# import os

# load_dotenv()
# os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# st.set_page_config(page_title="AI Website Generator", page_icon="🤧")
# st.title("PORTFOLIO WEBSITE GENERATOR")

# uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

# def extract_text_from_pdf(uploaded_file):
#     reader = PdfReader(uploaded_file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text() or ""
#     return text

# if st.button("Generate") and uploaded_file is not None:

#     resume_text = extract_text_from_pdf(uploaded_file)

#     model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

#     messages = [
#         SystemMessage(content="""
# You are an expert in generating a portfolio website from resume text.
# Extract name, skills, experience, projects, achievements, education,
# design style, and generate a colorful portfolio website.

# Output format must be:

# --html--
# [html code]
# --html--

# --css--
# [css code]
# --css--

# --js--
# [js code]
# --js--
# """),
#         HumanMessage(content=resume_text)
#     ]

#     response = model.invoke(messages)

#     # Save files
#     with open("index.html", "w", encoding="utf-8") as f:
#         f.write(response.content.split("--html--")[1])

#     with open("style.css", "w", encoding="utf-8") as f:
#         f.write(response.content.split("--css--")[1])

#     with open("script.js", "w", encoding="utf-8") as f:
#         f.write(response.content.split("--js--")[1])

#     # Zip files
#     with zipfile.ZipFile("website.zip", "w") as zipf:
#         zipf.write("index.html")
#         zipf.write("style.css")
#         zipf.write("script.js")

#     st.download_button(
#         "Click to download website",
#         data=open("website.zip", "rb"),
#         file_name="website.zip"
#     )

#     st.success("Website generated successfully")


# ============================================================
# AI RESUME → PORTFOLIO WEBSITE GENERATOR (ADVANCED STREAMLIT)
# ============================================================
# Features:
# - Resume (PDF) → Portfolio Website
# - Premium animated UI (blue–purple)
# - Glassmorphism cards
# - Resume summary preview
# - Robust LLM parsing
# - ZIP export (HTML/CSS/JS)

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import zipfile
from pypdf import PdfReader
from langchain_core.messages import SystemMessage, HumanMessage
import os

# ============================================================
# ENV SETUP
# ============================================================
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI Resume to Portfolio Generator",
    page_icon="✨",
    layout="centered"
)

# ============================================================
# ADVANCED UI STYLING
# ============================================================
st.markdown("""
<style>
@keyframes gradientBG {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}

.stApp {
  background: linear-gradient(-45deg, #eef2ff, #e0e7ff, #f5f3ff, #ede9fe);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
}

.glass {
  background: rgba(255,255,255,0.75);
  backdrop-filter: blur(18px);
  border-radius: 22px;
  padding: 2rem;
  box-shadow: 0 20px 40px rgba(99,102,241,0.25);
}

h1 {
  text-align: center;
  color: #1e1b4b;
  font-weight: 800;
}

.subtitle {
  text-align: center;
  color: #475569;
  margin-bottom: 1.5rem;
}

.stFileUploader {
  border-radius: 14px;
}

.stButton button {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  font-weight: 700;
  border-radius: 16px;
  padding: 0.8rem 2.2rem;
  border: none;
  box-shadow: 0 12px 28px rgba(99,102,241,0.45);
  transition: all 0.3s ease;
}

.stButton button:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 18px 38px rgba(139,92,246,0.6);
}

.success-box {
  background: #ecfeff;
  border-left: 6px solid #6366f1;
  border-radius: 14px;
  padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================
# st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.markdown("# 📄 Resume → Portfolio Website Generator")
st.markdown(
    "<p class='subtitle'>Upload your resume and instantly get a <b>modern, colorful, professional portfolio website</b>.</p>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type="pdf")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

generate = st.button("🚀 Generate Portfolio Website")

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# GENERATION LOGIC
# ============================================================
if generate:
    if uploaded_file is None:
        st.warning("Please upload a PDF resume.")
        st.stop()

    with st.spinner("✨ Analyzing resume & designing website..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

        messages = [
            SystemMessage(content="""
You are a senior UI/UX designer and expert frontend developer.

Task:
- Analyze resume text
- Extract name, role, summary, skills, experience, projects, education, achievements
- Generate a **visually stunning portfolio website**

Design rules:
- gradient theme
- Card-based layout
- Smooth hover animations
- Responsive design
- Professional typography

Tech rules:
- Pure HTML, CSS, JS only
- No frameworks

STRICT OUTPUT FORMAT:
--html--
[HTML]
--html--
--css--
[CSS]
--css--
--js--
[JS]
--js--
"""),
            HumanMessage(content=resume_text)
        ]

        response = model.invoke(messages)
        content = response.content

        try:
            html = content.split("--html--")[1].split("--css--")[0]
            css = content.split("--css--")[1].split("--js--")[0]
            js = content.split("--js--")[1]
        except Exception:
            st.error("⚠️ Failed to generate website. Try another resume.")
            st.stop()

        # Save files
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        with open("style.css", "w", encoding="utf-8") as f:
            f.write(css)
        with open("script.js", "w", encoding="utf-8") as f:
            f.write(js)

        # Zip
        with zipfile.ZipFile("portfolio_website.zip", "w") as zipf:
            zipf.write("index.html")
            zipf.write("style.css")
            zipf.write("script.js")

        st.markdown("<div class='success-box'>🎉 Website generated successfully!</div>", unsafe_allow_html=True)

        st.download_button(
            "⬇️ Download Portfolio Website (ZIP)",
            data=open("portfolio_website.zip", "rb"),
            file_name="portfolio_website.zip",
            mime="application/zip"
        )
