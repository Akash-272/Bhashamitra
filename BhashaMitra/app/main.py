import streamlit as st
from app.services.translation_service import translate_text
from app.services.simplification_service import simplify_text
from app.services.document_processing import extract_text_from_pdf
from app.services.voice_service import speak_text
from app.services.dialog_management import handle_user_query

st.set_page_config(page_title="BhashaMitra", layout="wide")

st.title("🇮🇳 BhashaMitra")
uploaded_file = st.file_uploader("Upload a Government Document (PDF/Text)", type=["pdf", "txt"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Document Text:", text, height=200)

    target_lang = st.selectbox("Translate to regional language:", ["Marathi", "Tamil", "Bengali"])
    translated = translate_text(text, target_lang)
    st.text_area("Translated Text:", translated, height=200)

    simplified = simplify_text(translated)
    st.text_area("Simplified Explanation:", simplified, height=200)

    user_query = st.text_input("Ask a question about the document (e.g., What is Clause 4?)")
    if user_query:
        response = handle_user_query(user_query, text, target_lang)
        st.text_area("Answer:", response, height=150)
        speak_text(response, target_lang)
