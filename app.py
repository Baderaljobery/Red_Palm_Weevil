import streamlit as st
import pandas as pd

st.set_page_config(page_title="Palm Dashboard", layout="wide")

st.title("🌴 Red Palm Weevil Dashboard")
st.markdown("""
<div style="
    background: linear-gradient(135deg, #0a4d26, #0e6833);
    color:white;
    padding:25px;
    border-radius:15px;
    font-size:19px;
    line-height:1.9;
">
    <h3>🌴 Symbol of the Kingdom of Saudi Arabia</h3>
    <p>
    The palm tree has been closely connected to humans since ancient times, serving as a companion in building civilization across the various environments in which it grows.
    It holds a significant place in social, economic, and cultural life.
    <br><br>
    And it is a great honor that the palm tree stands as one of the prominent symbols of the Kingdom of Saudi Arabia 🇸🇦🌴
    </p>
</div>
""",
unsafe_allow_html=True)


st.title("📊 Palm Dataset Overview")

# ------------ Load Data ------------
url = "https://raw.githubusercontent.com/Baderaljobery/Red_Palm_Weevil/refs/heads/main/dataset/finaldataset_Red_Palm_Weevil.csv"
df = pd.read_csv(url)

# ------------ Show Dataset ------------
st.subheader("📄 Dataset Preview")
st.dataframe(df, use_container_width=True)

# ------------ Instruction Box ------------
st.markdown("""
<br>
<div style="
    background-color:#f1f1f1;
    padding:18px;
    border-radius:12px;
    font-size:18px;
    text-align:center;
    color:#333;
">
<b>🔎 Please click on the (Analysis View) box on the left to view the analysis..</b>
</div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
/* تغيير لون الخلفية الأساسية */
[data-testid="stAppViewContainer"] {
    background-color: #f5efe6;
}

/* تغيير خلفية الشريط العلوي */
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}

/* تغيير خلفية الشريط الجانبي */
[data-testid="stSidebar"] {
    background-color: #faf4e6;
}
</style>
""", unsafe_allow_html=True)
