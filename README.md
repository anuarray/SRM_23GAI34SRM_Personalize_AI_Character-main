# Samsung PRISM Personalized Chatbot

This project is a personalized chatbot interface built using Streamlit and the Langchain Ollama model, designed to generate responses based on the user's mood and the role they select. The chatbot adapts its tone and style of response based on a combination of emotional context (mood) and perspective (role), providing a flexible and engaging user experience.

## Features

- **Dynamic Mood Selection**: The chatbot adapts its response tone based on the user's selected mood (e.g., Happy, Sad, Sorrow, Angry).
- **Role-Based Responses**: Users can choose the role from which the chatbot responds, such as Professor, Mentor, Friend, or Counselor.
- **Interactive UI**: A simple and user-friendly interface created using Streamlit.
- **Real-Time Response Generation**: Responses are generated dynamically in real time using the Ollama Llama3 model from the Langchain Community.

## Technologies Used

- **Python**: Main programming language for the project.
- **Streamlit**: Framework used to create an interactive and lightweight web app.
- **Langchain**: Integration of Ollama Llama3 model for natural language processing and response generation.

## Getting Started

### Prerequisites

Before running the project, you need to have the following installed:

- Python 3.8+
- Streamlit (`pip install streamlit`)
- Langchain Community (`pip install langchain_community`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/samsung-prism-chatbot.git
   cd samsung-prism-chatbot


### Steps to Complete:
- Create a `requirements.txt` with the following:
  ```txt
  langchain
  langchain_community
  streamlit
  
### Future Enhancements:
    Add more moods and roles for greater flexibility.
    Allow users to input custom moods and roles.
    Implement further customization of response style and content.
    Deploy the app for broader accessibility via cloud hosting platforms. 
