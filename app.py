from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

## When submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)  

# from dotenv import load_dotenv
# import os
# import google.generativeai as genai

# # Load environment variables from .env file
# load_dotenv()

# # Get API key from environment variables
# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     raise ValueError("API Key not found. Please set GOOGLE_API_KEY in the .env file.")

# # Configure the Generative AI API
# genai.configure(api_key=api_key)

# # Create the generative model instance
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Generate content
# response = model.generate_content("Explain how AI works")

# # Print the response
# print(response.text)

