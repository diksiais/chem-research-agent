import streamlit as st
import requests
from prompts import format_research_prompt

# Replace with your own Hugging Face token
HUGGINGFACE_TOKEN = "YOUR_HF_TOKEN"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}"
}

def query_model(prompt):
    response = requests.post(API_URL, headers=headers, json={
        "inputs": prompt,
        "parameters": {"temperature": 0.7, "max_new_tokens": 300}
    })

    if response.status_code != 200:
        return f"⚠️ Error: {response.status_code} - {response.text}"
    
    return response.json()[0]["generated_text"]

# Streamlit UI
st.title("🔬 AI Research Agent for Chemists")

topic = st.text_input("🔍 Research Topic")
goal = st.text_area("🎯 Research Goal")
data = st.text_area("🧪 Data We Already Have")

if st.button("💡 Generate Research Ideas"):
    if not topic or not goal or not data:
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Generating ideas..."):
            prompt = format_research_prompt(topic, goal, data)
            ideas = query_model(prompt)
            st.subheader("✅ Suggested Research Ideas")
            st.markdown(ideas)
