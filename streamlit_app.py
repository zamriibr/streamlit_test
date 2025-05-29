import streamlit as st 
# Set the app title 
st.title('My First Streamlit App') 
# Add a welcome message 
st.write('Welcome to my Streamlit app!') 
# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
st.write('Customized Message:', user_input)
