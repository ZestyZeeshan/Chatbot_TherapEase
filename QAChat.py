from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini Pro model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Function to load Gemini Pro model and get responses
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(
    page_title="TherapEase: Your Mental Wellness Ally",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Background Styling */
    .stApp {
        background-color: #1a2b50; /* Royal navy-blue */
        background-image: url('https://www.transparenttextures.com/patterns/black-linen.png'); /* Subtle pattern */
        background-size: cover;
        background-repeat: repeat;
        background-attachment: fixed;
    }
    /* Main Title */
    .main-title {
        color: #fdfdfd;
        text-align: center;
        font-size: 3.5em;
        font-weight: bold;
        margin-top: 20px;
        text-shadow: 2px 2px 4px #000000;
    }
    /* Input and Button Container */
    .input-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 30px 0;
    }
    .input-container input {
        width: 60%;
        padding: 15px;
        border-radius: 10px;
        background-color: #ffffff;
        border: 2px solid #4a5a89;
        font-size: 1.2em;
        margin-right: 20px;
    }
    .input-container button {
        background-color: #56c596;
        color: #ffffff;
        font-size: 1.5em;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 20px 40px; /* Enlarged button */
        cursor: pointer;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
        transition: background-color 0.3s ease;
    }
    .input-container button:hover {
        background-color: #72d1ab;
    }
    /* Latest Conversation */
    .latest-conversation-heading {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        color: #ffffff;  /* Changed to white */
        margin-top: 20px;
    }
    .latest-conversation {
        # text-align: center;
        font-size: 1.5em; /* Increased font size */
    }
    .latest-conversation .user {
        color: #f8e71c; /* Yellow color for the user */
        font-weight: bold;
    }
    .latest-conversation .bot {
        color: #56c596; /* Light green for bot */
        font-weight: normal;
    }
    /* Chat History */
    .chat-history-heading {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        color: #fdfdfd;
        margin-top: 40px;
    }
    .chat-history {
        text-align: center;
        font-size: 1.2em;
        color: #f2a5d1; /* Light color for bot */
    }
    .chat-message {
        margin-bottom: 15px;
    }
    .chat-message .user {
        color: #f8e71c; /* Yellow color for the user */
        font-weight: bold;
    }
    .chat-message .bot {
        color: #56c596; /* Light green for bot */
        font-weight: normal;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown('<div class="main-title">TherapEase: Your Mental Wellness Ally</div>', unsafe_allow_html=True)

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input section with Ask button on the same line
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2 = st.columns([5, 1])
with col1:
    input_text = st.text_input(
        "",
        key="input",
        placeholder="Type your question here...",
        help="Ask your mental health-related question.",
        label_visibility="collapsed",
    )
with col2:
    submit = st.button("Ask", key="submit", help="Click to get the response")
st.markdown('</div>', unsafe_allow_html=True)

# Chat functionality
if submit and input_text:
    response = get_gemini_response(input_text)
    # Add user query to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    # Combine all chunks of the response into a single string
    bot_response = "".join(chunk.text for chunk in response)
    # Add bot response to session state chat history
    st.session_state['chat_history'].append(("Bot", bot_response))

    # Display the latest conversation heading and bot's response
    st.markdown('<div class="latest-conversation-heading">How can I assist you today?</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="latest-conversation"><span class="user">You:</span> {input_text}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="latest-conversation"><span class="bot">Bot:</span> {bot_response}</div>', unsafe_allow_html=True)

# Display the full chat history heading and history content
if st.session_state['chat_history']:
    st.markdown('<div class="chat-history-heading">Chat History</div>', unsafe_allow_html=True)
    for role, text in st.session_state['chat_history']:
        if role == "You":
            st.markdown(f'<div class="chat-message"><span class="user">{role}:</span> {text}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message"><span class="bot">{role}:</span> {text}</div>', unsafe_allow_html=True)



# Old code previous with gemini

# from dotenv import load_dotenv
# load_dotenv() ## loading all the environment variables

# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## function to load Gemini Pro model and get repsonses
# model=genai.GenerativeModel("gemini-1.5-flash") 
# chat = model.start_chat(history=[])
# def get_gemini_response(question):
    
#     response=chat.send_message(question,stream=True)
#     return response

# ##initialize our streamlit app

# st.set_page_config(page_title="Chatbot")

# st.header("TharapEase : Your Mental Wellness Ally")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input=st.text_input("Input: ",key="input")
# submit=st.button("Ask the question")

# if submit and input:
#     response=get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Bot", chunk.text))
# st.subheader("Chat History:")
    
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}:{text}")
    
    
    