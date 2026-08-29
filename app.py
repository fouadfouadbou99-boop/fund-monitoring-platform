import streamlit as st

from extraction.pdf_reader import extract_text_from_pdf
from extraction.docx_reader import extract_text_from_docx

from ai.extractor import analyze_document

from database import (
    init_db,
    save_analysis
)


init_db()

st.set_page_config(
    page_title="Suivi Fonds PE & OPCI",
    page_icon="📊",
    layout="wide"
)

st.title(
    "📊 Suivi Fonds PE & OPCI"
)

uploaded_file = st.file_uploader(
    "Déposer un reporting",
    type=[
        "pdf",
        "docx"
    ]
)

if uploaded_file:

    st.info(
        f"Document : {uploaded_file.name}"
    )

    if uploaded_file.name.lower().endswith(
        ".pdf"
    ):

        text = extract_text_from_pdf(
            uploaded_file
        )

    else:

        text = extract_text_from_docx(
            uploaded_file
        )

    st.success(
        f"Texte extrait : {len(text)} caractères"
    )

    with st.spinner(
        "Analyse IA en cours..."
    ):

        result = analyze_document(
            text
        )

    st.success(
        "Analyse terminée"
    )

    st.subheader(
        "JSON extrait"
    )

    st.json(result)

    if "alertes" in result:

        if result["alertes"]:

            st.subheader(
                "🚨 Alertes"
            )

            for alerte in result["alertes"]:

                st.warning(
                    str(alerte)
                )

    if "gouvernance" in result:

        st.subheader(
            "👥 Gouvernance"
        )

        st.json(
            result["gouvernance"]
        )

    projet = (
        result
        .get(
            "informations_generales",
            {}
        )
        .get(
            "nom_projet",
            "Inconnu"
        )
    )

    save_analysis(
        uploaded_file.name,
        projet,
        result
    )

    st.success(
        "Analyse enregistrée dans la base."
    )
