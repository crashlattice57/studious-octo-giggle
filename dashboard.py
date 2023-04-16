import pandas as pd
import plotly.express as px
import streamlit as st

from data_cleaning import clean_data

st.set_page_config(page_title="Cyber Attack Dashboard 2005-2022", page_icon=":bar_chart:", layout="wide")


## Load and Cache Data
@st.cache_data
def load_data():
    return clean_data()


df = load_data()

## ---------------- SIDEBAR ------------------------ ##

st.sidebar.header("Please Filter Here:")
category = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

sponsor = st.sidebar.multiselect(
    "Select Attack Sponsor:",
    options=df["Sponsor"].unique(),
    default=df["Sponsor"].unique()
)

affiliations = st.sidebar.multiselect(
    "Select Attack Affiliation:",
    options=df["Affiliations"].unique(),
    default=df["Affiliations"].unique()
)

df_selection = df.query("Category == @category &"
                        " Sponsor == @sponsor &"
                        " Affiliations == @affiliations")

#st.dataframe(df_selection)

## -----------------------------------  MAINPAGE ------------------------ ##
st.title("Cyber Attack Dashboard")
st.markdown("##")

# TOP KPI's
total_attacks = int(len(df_selection["Title"].unique()))
top_sponsor = df["Sponsor"].value_counts().index.tolist()[0]
top_victim = df["Victims"].value_counts().index.tolist()[0]

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Attacks")
    st.subheader(f"{total_attacks}")

with middle_column:
    st.subheader("Top Sponsor")
    st.subheader(top_sponsor)

with right_column:
    st.subheader("Top Victim")
    st.subheader(top_victim)

st.markdown("---")

## Attacks by Year Chart ""

attacks_by_year = (df_selection.groupby(by=["Year"])["Title"].nunique())
fig_attacks_by_year = px.line(attacks_by_year,
                              y="Category",
                              x=attacks_by_year.index,
                              orientation="h",
                              title="<b>Attacks by Year</b>",
                              color_discrete_sequence=["#0083B8"] * len(attacks_by_year),
                              template="plotly_white")

fig_attacks_by_year.update_layout(plot_bgcolor="rgba(0,0,0,0)",
                                  xaxis=(dict(showgrid=False)))

st.plotly_chart(fig_attacks_by_year)
