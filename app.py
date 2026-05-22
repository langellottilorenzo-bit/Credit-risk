import streamlit as st
import pandas as pd
from src.kpis import calculate_kpis
from src.plots import plot_pd_distribution, plot_el_by_segment, plot_ead_lgd

st.set_page_config(page_title="Credit Risk Dashboard", layout="wide")

st.title("🏦 Credit Risk Dashboard")

uploaded_file = st.file_uploader("Upload portfolio data", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/portfolio.csv")

st.sidebar.header("Filters")
segment = st.sidebar.selectbox("Segment", ["All"] + list(df["Segment"].unique()))

if segment != "All":
    df = df[df["Segment"] == segment]

kpis, df = calculate_kpis(df)

st.subheader("📊 Key Risk Indicators")
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total EAD", f"{kpis['Total EAD']:,.0f}")
col2.metric("Expected Loss", f"{kpis['Expected Loss']:,.0f}")
col3.metric("NPL Ratio", f"{kpis['NPL Ratio']:.2%}")
col4.metric("Coverage Ratio", f"{kpis['Coverage Ratio']:.2%}")
col5.metric("Cost of Risk", f"{kpis['Cost of Risk']:.2%}")

st.subheader("📈 Visual Analytics")
colA, colB = st.columns(2)

with colA:
    st.pyplot(plot_pd_distribution(df))

with colB:
    st.pyplot(plot_el_by_segment(df))

st.pyplot(plot_ead_lgd(df))
