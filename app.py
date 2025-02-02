from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model="llama3")

st.title("Samsung PRISM Personalized Chatbot")

mood = st.selectbox("How are you feeling currently?", ["Happy", "Sad", "Sorrow", "Angry"])
role = st.selectbox("Select the role for response generation:", ["Professor", "Mentor", "Friend", "Counselor"])

prompt = st.text_area("Enter your query:")


def generate_response(prompt, mood, role):
    mood_prefix = {
        "Happy": "Respond in a happy tone: ",
        "Sad": "Respond in a sad tone: ",
        "Sorrow": "Respond in a sorrowful tone: ",
        "Angry": "Respond in an angry tone: "
    }

    role_instructions = {
        "Professor": "Answer as a professor with a deep understanding of the subject, providing academic insight: ",
        "Mentor": "Answer as a mentor with guidance, encouragement, and practical advice: ",
        "Friend": "Answer as a close friend, providing empathy and informal advice: ",
        "Counselor": "Answer as a counselor, offering support and thoughtful advice: "
    }

    complete_prompt = mood_prefix.get(mood, "") + role_instructions.get(role, "") + prompt
    return llm.invoke(complete_prompt, stop=['<|eot_id|>'])


if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            response = generate_response(prompt, mood, role)
            st.write(response)
