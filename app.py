import json

import streamlit as st

from extraction.pdf_reader import extract_text_from_pdf

from extraction.docx_reader import extract_text_from_docx

from ai.extractor import analyze_document

st.set_page_config(

    page_title="Fund Monitoring",

    layout="wide"

)

st.title("📊 Monitoring Fonds PE & OPCI")

uploaded_file = st.file_uploader(

    "Déposer un reporting",

    type=["pdf", "docx"]

)

if uploaded_file:

    if uploaded_file.name.endswith(".pdf"):

        text = extract_text_from_pdf(uploaded_file)

    else:

        text = extract_text_from_docx(uploaded_file)

    with st.spinner("Analyse IA en cours..."):

        result = analyze_document(text)

    st.success("Analyse terminée")

    try:

        parsed = json.loads(result)

        st.json(parsed)

    except:

        st.write(result)
