import streamlit as st
import pandas as pd
import openai_helper

col1, col2 = st.columns([3,2])

job_Description_df = pd.DataFrame({
        "Classes": ["Education", "Languages", "Technical Skills", "Soft Skills", "Technology and Concepts"],
        "Keywords": ["", "", "", "", ""]
    })

with col1:
    st.title("ATS Friendly Keyword Extractor")
    job_description = st.text_area("Paste your Job Description here", height=500)
    if st.button("Extract"):
        job_Description_df = openai_helper.extract_Keywords(job_description)

with col2:
    st.markdown("<br/>" * 5, unsafe_allow_html=True)  # Creates 5 lines of vertical space
    st.dataframe(
        job_Description_df,
        column_config={
            "Classes": st.column_config.Column(width=150),
            "keywords": st.column_config.Column(width=400)
        },
        hide_index=True
    )