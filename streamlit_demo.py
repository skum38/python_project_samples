import streamlit as str
str.title("Streamlit API Demo")
str.write("This is a demo of a Streamlit application that interacts with users.")
input=str.text_input("Enter your name:", key="name_input")
if str.button("Greet Me"):
    name=str.session_state.name_input
    str.write(f"Hello, {name}! Welcome to the Streamlit API Demo.")
