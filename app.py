import streamlit as st
import os
from groq.client import Groq

# Initialize Groq client using the API key (replace with your actual API key)
client = Groq(api_key="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")

# Function to get feedback from the Groq model
def get_feedback(user_essay, level):
    # Example of sending the essay to Groq's API (you will need to adjust this based on Groq's API)
    response = client.completions.create(
        prompt=f"Analyze this essay for {level} level English: {user_essay}",
        max_tokens=1000
    )
    feedback = response["choices"][0]["text"]
    return feedback

# Streamlit app UI
st.title("Essay Writing Assistant for IELTS, DET, and TOEFL")

# Dropdown for selecting the plan
plan = st.selectbox("Select Your Plan", ["30 Days Plan", "45 Days Plan", "60 Days Plan"])

# Display the current day of the plan
st.write(f"Today's essay prompt for the {plan}:")

# Text area for students to write their essay
user_essay = st.text_area("Write your essay here:", height=300)

# Dropdown to select student's English proficiency level
level = st.selectbox("Select your English proficiency level", ["A1", "A2", "B1", "B2", "C1"])

# Submit button
if st.button("Submit"):
    if user_essay.strip() == "":
        st.error("Please write your essay before submitting!")
    else:
        # Fetch feedback from Groq API
        try:
            feedback = get_feedback(user_essay, level)
            st.success("Feedback received!")
            st.write(feedback)
        except Exception as e:
            st.error(f"Error fetching feedback: {e}")

# Instruction for deploying Streamlit (in case of Google Colab use)
st.write("To view this app in a browser, run with:")
st.code("!streamlit run app.py & npx localtunnel --port 8501")
