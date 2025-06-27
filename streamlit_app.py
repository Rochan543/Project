import streamlit as st
from app.dashboard import load_data

st.title("📊 Presence Tracking Dashboard")

st.markdown("View emotion and attendance logs captured via real-time video analytics.")

df = load_data()

if df.empty:
    st.warning("No log data found. Run the detection script first.")
else:
    st.subheader("📋 Log Table")
    st.dataframe(df)

    st.subheader("📈 Emotion Summary")
    emotion_counts = df["Emotion"].value_counts()
    st.bar_chart(emotion_counts)
