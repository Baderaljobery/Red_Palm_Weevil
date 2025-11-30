import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/Baderaljobery/Red_Palm_Weevil/refs/heads/main/dataset/finaldataset_Red_Palm_Weevil.csv"
df = pd.read_csv(url)

st.title("1- What is the rate of region examined for the year 2024 ?")
st.write("ok")

#1
fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(data=df, x="Region", y="2024_inspection", ax=ax)

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_title("Number of inspections in 2024")
ax.set_xlabel("Region")
ax.set_ylabel("Number of inspections in 2024")
plt.tight_layout()

st.pyplot(fig)
#-------------------------------------------------
st.title("2- How many palm trees were inspected in 2019 ?")
total_2019 = df['2019_inspection'].sum()

st.metric(
    label="Total Inspections in 2019",
    value=f"{total_2019:,}"
)
