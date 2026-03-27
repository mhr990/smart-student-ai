import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Smart Student AI", page_icon="🎓")

# 1. Enter your real key inside the quotes below
api_key = st.secrets["GEMINI_KEY"]

st.title("🎓 Smart Student AI Assistant")
st.markdown("### Welcome! Paste your lesson below to begin.")

text = st.text_area("Enter your lesson or paragraph:", height=200)

if text:
    if api_key == "PASTE_YOUR_GEMINI_KEY_HERE":
        st.error("❌ You forgot to put your real API key in the code!")
    else:
        # Configure Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        col1, col2, col3 = st.columns(3)
        
        if col1.button("💡 Explain"):
            with st.spinner("Explaining..."):
                response = model.generate_content(f"Explain this simply: {text}")
                st.success("### Explanation")
                st.write(response.text)

        if col2.button("📝 Summarize"):
            with st.spinner("Summarizing..."):
                response = model.generate_content(f"Summarize this in bullets: {text}")
                st.success("### Summary")
                st.write(response.text)

        if col3.button("❓ Quiz Me"):
            with st.spinner("Creating questions..."):
                response = model.generate_content(f"Generate 3 quiz questions for: {text}")
                st.success("### Practice Questions")
                st.write(response.text)
