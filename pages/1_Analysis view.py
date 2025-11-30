import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/Baderaljobery/Red_Palm_Weevil/refs/heads/main/dataset/finaldataset_Red_Palm_Weevil.csv"
df = pd.read_csv(url)

st.title("1- What is the rate of region examined for the year 2024 ?")
st.write("")

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
#-------------------------------------------------
st.markdown("""
<hr style="border: 2px solid #0a5c2d;">
""", unsafe_allow_html=True)
#-------------------------------------------------
st.title("5- What was the growth rate in 2022 compared to the previous year?")
growth_2020 = ((df["2020_inspection"] - df["2019_inspection"]) / df["2019_inspection"]) * 100
growth_2020.index = df["Region"]

growth_2020_formatted = growth_2020.apply(lambda x: f"{x:.2f}%")

# ============= Display =============
st.subheader("📈 Growth Rate in 2020 by Region")

st.dataframe(
    growth_2020_formatted.to_frame("Growth 2020 (%)"),
    use_container_width=True
)
#-------------------------------------------------
st.markdown("""
<hr style="border: 2px solid #0a5c2d;">
""", unsafe_allow_html=True)
#-------------------------------------------------
st.title("6- What is the percentage of affected region in 2024?")
infection_rate_2024_percent = (
    df["Infected_palm_2024"] / df["2024_inspection"] * 100
)
fig, ax = plt.subplots(figsize=(10,7))

sns.barplot(
    y="Region",
    x=infection_rate_2024_percent,
    data=df,
    palette="Reds_r",
    ax=ax
)

ax.set_xlabel("Infection Rate 2024 (%)")
ax.set_ylabel("Region")
ax.set_title("Palm Infection Rate by Region - 2024")

plt.tight_layout()
st.pyplot(fig)
#-------------------------------------------------
st.markdown("""
<hr style="border: 2px solid #0a5c2d;">
""", unsafe_allow_html=True)
#-------------------------------------------------
st.title("7- What is the mean from 2019 - 2024 ?")
st.subheader("📊 Mean of All Numeric Columns")

inspection_cols = df.filter(like="inspection").columns
inspection_mean = df[inspection_cols].mean()

st.dataframe(inspection_mean.to_frame("Mean"), use_container_width=True)

#-------------------------------------------------
st.markdown("""
<hr style="border: 2px solid #0a5c2d;">
""", unsafe_allow_html=True)
#-------------------------------------------------
st.title("8- What is the relationship between the inspected, infected, and treated palm trees?")
# ======= الرسم =======
fig, ax = plt.subplots(figsize=(12, 7))

sns.scatterplot(
    data=df,
    x="2024_inspection",
    y="Infected_palm_2024",
    size="Treated_palm_2024",
    hue="Region",
    sizes=(50, 800),
    alpha=0.7,
    ax=ax
)

ax.set_xlabel("Inspected Palms 2024")
ax.set_ylabel("Infected Palms 2024")
ax.set_title("Inspection vs Infection vs Treatment (2024) by Region")

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

st.pyplot(fig)
