import openai
import os
import streamlit as st
from Api_Key import openai_api_key

openai.api_key = openai_api_key

messages = []
messages.append({"role": "system", "content": "You are a grocery chatbot help the user by provideing detailed information on various grocery products, such as nutritional content, ingredients, and allergens, and evenif the user asks about certain thing you gave the products names (like cocacola and so on) helping users make informed purchasing decisions"})

while True:
    message = st.text_input("Enter your message:")
    if message == "quit()":
        break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    st.write(reply)