import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/USERNAME/REPO/main/data/dataset.csv"
df = pd.read_csv(url)

st.title("السؤال 1: [اكتب السؤال]")
st.write("شرح بسيط…")

plt.figure(figsize=(10, 5))

sns.barplot(data=df, x="Region", y="2024_inspection")

plt.xticks(rotation=45, ha="right")
plt.title("Number of inspections in 2024")
plt.xlabel("Region")
plt.ylabel("Number of inspections in 2024")
plt.tight_layout()
plt.show()
