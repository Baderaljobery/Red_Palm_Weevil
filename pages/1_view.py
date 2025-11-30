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
st.markdown("""
<hr style="border: 2px solid #0a5c2d;">
""", unsafe_allow_html=True)
#-------------------------------------------------
st.title("2- How many palm trees were inspected in 2019 ?")
total_2019 = df['2019_inspection'].sum()

st.metric(
    label="Total Inspections in 2019",
    value=f"{total_2019:,}"
)
#-------------------------------------------------
st.markdown("""
<hr style="border: 2px solid #0a5c2d;">
""", unsafe_allow_html=True)
#-------------------------------------------------
st.title("3- What is the percentage of infected palm trees for the year 2023?")
infection_rate_2023_percent = (
    df["Infected_palm_2023"] / df["2023_inspection"] * 100
)

plot_df = pd.DataFrame({
    "Region": df["Region"],
    "Infection_Rate_2023": infection_rate_2023_percent
})

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(plot_df["Region"], plot_df["Infection_Rate_2023"], color='skyblue')

ax.set_xlabel("Region")
ax.set_ylabel("Infection Rate (%)")
ax.set_title("Infection Rate of Palm Weevil in 2023 by Region")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)
#-------------------------------------------------
st.markdown("""
<hr style="border: 2px solid #0a5c2d;">
""", unsafe_allow_html=True)
#-------------------------------------------------
st.title("4- What was the region with the highest number of palm trees in 2022?")
max_idx = df["2022_inspection"].idxmax()
region = df.loc[max_idx, "Region"]
value  = df.loc[max_idx, "2022_inspection"]

st.metric(
    label="Region with Highest Inspections in 2022",
    value=f"{value:,}",
    delta=region
)
