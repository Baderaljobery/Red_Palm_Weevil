import streamlit as st

st.set_page_config(page_title="Palm Dashboard", layout="wide")

st.title("🌴 Palm Inspection Dashboard")
st.markdown("""
<div style="
    background: linear-gradient(135deg, #0a4d26, #0e6833);
    color:white;
    padding:25px;
    border-radius:15px;
    font-size:19px;
    line-height:1.9;
">
    <h3>🌴 رمز المملكة العربية السعودية</h3>
    <p>
    ارتبطت النخلة بالإنسان منذ الأزل وكانت رفيقته في بناء الحضارة في مختلف البيئات التي تنمو فيها ولها مكانة عظيمة في الحياة الإجتماعية والإقتصادية والثقافية.
    <br><br>
    ويكفي فخرًا أنها رمز من رموز المملكة العربية السعودية 🇸🇦🌴
    </p>
</div>
""",
unsafe_allow_html=True)

