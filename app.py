import streamlit as st

st.set_page_config(
    page_title="Job Recommendation System",
    page_icon="💼",
    layout="centered"
)

# Background Image
page_bg = """
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.main-box {
    background: rgba(0, 0, 0, 0.65);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
}

h1, h2, h3, p, label {
    color: white !important;
}

textarea {
    background-color: white !important;
    color: black !important;
}

.stButton > button {
    width: 100%;
    background-color: #00b4d8;
    color: white;
    border-radius: 10px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.markdown("""
<div class="main-box">
<h1>💼 Job Recommendation System</h1>
<p>Enter your skills or resume summary to get a recommended job role.</p>
</div>
""", unsafe_allow_html=True)

skills = st.text_area(
    "Enter Skills / Resume Summary",
    height=180
)

if st.button("Recommend Job"):

    if skills.strip() == "":
        st.warning("Please enter your skills.")

    else:

        text = skills.lower()

        if any(word in text for word in
               ["python", "machine learning", "deep learning", "tensorflow", "pandas"]):
            job = "Data Scientist"

        elif any(word in text for word in
                 ["sql", "power bi", "tableau", "excel"]):
            job = "Data Analyst"

        elif any(word in text for word in
                 ["java", "spring", "hibernate"]):
            job = "Java Developer"

        elif any(word in text for word in
                 ["html", "css", "javascript", "react"]):
            job = "Web Developer"

        elif any(word in text for word in
                 ["aws", "docker", "kubernetes", "devops"]):
            job = "DevOps Engineer"

        elif any(word in text for word in
                 ["c++", "c", "data structures", "algorithms"]):
            job = "Software Engineer"

        else:
            job = "Software Developer"

        st.success(f"🎯 Recommended Job: {job}")
