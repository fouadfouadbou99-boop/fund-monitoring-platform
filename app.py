import streamlit as st
import google.generativeai as genai

st.title("Modèles Gemini")

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

for model in genai.list_models():
    try:
        st.write(model.name)
        st.write(model.supported_generation_methods)
        st.write("---")
    except:
        pass
