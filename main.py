import pandas as pd
import streamlit as st

df = pd.read_csv("student.csv")

st.title("Raw Data")
st.write(df)


df.drop_duplicates(inplace=True)


df["math_score"] = pd.to_numeric(
    df["math_score"],
    errors="coerce"
)

df.fillna(df.mean(numeric_only=True), inplace=True)

df["name"].fillna("Unknown", inplace=True)

st.subheader("Cleaned Data")
st.write(df)

avg_math = df["math_score"].mean()

topper = df.loc[df["math_score"].idxmax()]

st.metric("Average Math Score", round(avg_math, 2))

st.write("Topper:")
st.write(topper)

st.bar_chart(df["math_score"])