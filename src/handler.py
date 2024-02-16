from dotenv import load_dotenv

load_dotenv()

#import streamlit as st
import os
import google.generativeai as genai

#api_key = os.getenv("GOOGLE_API_KEY")
#print(api_key)
genai.configure(api_key="XXX")

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        print(response)
        text_response = ''
        if isinstance(response.text, str):
            text_response = response.text
        else:
            text_response = ' '.join(part for part in response.text.parts)  # assuming response.text.parts is a list of strings

        # Limit the response to 300 words
        words = text_response.split()
        if len(words) > 100:
            text_response = ' '.join(words[:100]) + '... (response truncated)'

        return {'status': 1, 'response': text_response}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'status': 0, 'response': f"An error occurred: {e}"}
