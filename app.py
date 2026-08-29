import streamlit as st
import google.generativeai as genai

st.title("Modèles Gemini disponibles")

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

try:
    for model in genai.list_models():
        st.write(model.name)

except Exception as e:
    st.error(str(e))
