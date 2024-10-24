import os
import streamlit as st
from groq import Groq

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Function to get feedback from Groq API
def get_feedback(user_essay, level):
    # Define the system prompt for essay feedback
    system_prompt = """
    You are an expert academic writer with 40 years of experience in providing concise but effective feedback.
    Instead of asking the student to do this and that, you just say replace this with this to improve in a concise manner.
    You provide concise grammar mistakes, saying replace this with this along with mistake type. 
    You also provide specific replacement sentences for cohesion and abstraction, and you point out all the vocabulary saying replace this word with this.
    You have to analyze the writing for grammar, cohesion, sentence structure, vocabulary, and the use of simple, complex, and compound sentences, as well as the effectiveness of abstraction.
    Provide detailed feedback on any mistakes and present an improved version of the writing.
    Do not use words such as dive, discover, uncover, delve, tailor, equipped, navigate, landscape, delve, magic, comprehensive embrace, well equipped, unleash, cutting edge, harness.
    Strictly follow academic style in writing. Change the sentences according to English standards if needed but do not add any sentences by yourself.
    Give feedback for different levels: A1 for beginners, A2 for average, A3 for advanced, up to C1 level.
    """

    # Sending the essay and level to Groq API
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{system_prompt}\nEssay:\n{user_essay}\nLevel: {level}"
            }
        ],
        model="llama3-8b-8192"
    )
    
    # Extract feedback from API response
    feedback = response.choices[0].message.content
    return feedback

# Streamlit UI
st.title("Writing Assistant for IELTS/TOEFL/DET Preparation")

# Sidebar for selecting a plan
st.sidebar.title("Select Your Writing Plan")
plan = st.sidebar.radio("Choose a Plan", ("30 Days Plan", "45 Days Plan", "60 Days Plan"))

# Display plan details
if plan == "30 Days Plan":
    st.sidebar.write("Write every day for 30 days and get daily feedback on your essays.")
elif plan == "45 Days Plan":
    st.sidebar.write("Write every day for 45 days and improve your writing progressively.")
else:
    st.sidebar.write("A comprehensive 60 days writing improvement plan for advanced learners.")

# Show the current day based on the selected plan (for simplicity, showing Day 1 here)
st.subheader(f"Day 1 of {plan}")
st.write("Topic: Discuss a recent technological advancement and its impact on society.")

# Textbox for the user to input their essay
user_essay = st.text_area("Write your essay here:", height=300)

# Dropdown to select proficiency level
level = st.selectbox("Select your proficiency level:", ["A1 (Beginner)", "A2 (Average)", "B1", "B2", "C1 (Advanced)"])

# Button to submit essay for feedback
if st.button("Submit for Feedback"):
    if user_essay.strip():
        st.write("Analyzing your essay...")

        # Get feedback using the get_feedback function
        feedback = get_feedback(user_essay, level)
        
        # Display the feedback provided by the model
        st.subheader("Feedback on your essay:")
        st.write(feedback)
    else:
        st.warning("Please write your essay before submitting!")
