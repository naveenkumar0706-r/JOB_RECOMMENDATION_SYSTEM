import streamlit as st
import numpy as np
import pickle

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Page Config
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
    background: rgba(0,0,0,0.65);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 20px;
}

h1,p,label{
    color:white !important;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Load Model
@st.cache_resource
def load_files():

    model = load_model("job_model.h5")

    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    with open("label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)

    return model, tokenizer, label_encoder

model, tokenizer, label_encoder = load_files()

MAX_LEN = 200

st.markdown("""
<div class="main-box">
<h1>💼 Job Recommendation System</h1>
<p>Enter your skills or resume summary to get a recommended job role.</p>
</div>
""", unsafe_allow_html=True)

skills = st.text_area(
    "Enter Skills / Resume Summary",
    height=200
)

if st.button("Recommend Job"):

    if skills.strip() == "":
        st.warning("Please enter skills.")
    else:

        seq = tokenizer.texts_to_sequences([skills])

        padded = pad_sequences(
            seq,
            maxlen=MAX_LEN,
            padding="post"
        )

        prediction = model.predict(
            padded,
            verbose=0
        )

        predicted_class = np.argmax(prediction)

        job = label_encoder.inverse_transform(
            [predicted_class]
        )[0]

        confidence = np.max(prediction) * 100

        st.success(f"🎯 Recommended Job: {job}")
        st.info(f"Match Confidence: {confidence:.2f}%")
