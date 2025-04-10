import streamlit as st
from backend.model_router import route_model_conversion

st.set_page_config(
    page_title="C# to Java with Large Language Models 🌈",
    layout="wide",
    page_icon="✨"
)

st.markdown("""
    <div style="text-align: center; padding: 20px 10px;">
        <h1 style="color: #6C63FF; font-size: 3em;">🦄 The Enchanted Code Converter: .NET to Java</h1>
        <p style="color: #999; font-size: 1.2em;">✨ "Code it like a CEO. Convert it like a GEN_AI Innovator." ✨</p>
        <p style="color: #FF69B4;">The cutest way to switch your code from serious C# to jazzy Java 💃</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border-top: 2px dashed #eee;'>", unsafe_allow_html=True)

st.subheader("🪄 Choose your Magic Model:")
model_option = st.selectbox(
    "✨ Yours model box:",
    options=[
        "mistralai/Mistral-7B-Instruct-v0.2",
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "Salesforce/codegen2-1B"
    ],
    index=0
)

st.markdown("#### 🖊️ Paste your <span style='color:#6C63FF;'>C# Code</span> below:", unsafe_allow_html=True)
cs_code = st.text_area("📥 Your C# Code", height=250, placeholder="// Type some cool C# code...")

convert = st.button("✨ Convert with LLM's ✨")

if convert:
    with st.spinner("🧠 PowerBrain is thinking... sprinkling AI dust... 💭✨"):
        result = route_model_conversion(model_option, cs_code)
        if result:
            st.balloons()
            st.success("💃 Tadaa! Here's your Java code, boss!")
            st.code(result, language="java")
        else:
            st.error("🚨 Oopsie daisy! Something went wrong... maybe the code got shy? 🥺")

st.markdown("""
    <hr style="border-top: 2px solid #eee;">
    <div style='text-align: center; color: #aaa; font-size: 0.9em;'>
        🛠️ Made with Large Language Models by <br>
        <span style="font-size: 1.3em; font-weight: bold; color: #6C63FF;">Apoorva Vutukuru</span> ✨ <br>
        <i>Crafted for GEN_AI Innovators everywhere!</i>
    </div>
""", unsafe_allow_html=True)
