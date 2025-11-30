import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/Baderaljobery/Red_Palm_Weevil/refs/heads/main/dataset/finaldataset_Red_Palm_Weevil.csv"
df = pd.read_csv(url)

st.title("Q1 is ......")
st.write("sleep is goood")

#1
fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(data=df, x="Region", y="2024_inspection", ax=ax)

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_title("Number of inspections in 2024")
ax.set_xlabel("Region")
ax.set_ylabel("Number of inspections in 2024")
plt.tight_layout()

st.pyplot(fig)

