import streamlit as st
import os
import google.generativeai as genai
# Function to simulate a chatbot response
genai.configure(api_key=os.environ["google_api"])

model = genai.GenerativeModel('gemini-1.5-flash')

def get_bot_response(user_input):
        response = model.generate_content("you are a customer support bot  for CUSTOPS a company which provides users with software solutions related to customer services. the user asks \""+user_input)
        return(response)
    # Replace this with your actual chatbot logic
    # Return the response if it's in the dictionary, otherwise a default message


# Streamlit UI
st.title("CUSTOPS CHAT")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input box for user to type messages
user_input = st.text_input("You:", "")

# Submit button
if st.button("Send"):
    if user_input:
        # Append user message to chat history
        st.session_state.chat_history.append({"user": user_input})
        # Get bot response
        bot_response = get_bot_response(user_input)
        # Append bot response to chat history
        st.session_state.chat_history.append({"bot": bot_response})
        # Clear the input box
        st.text_input("You:", "", key="new_input")

# Display chat history
for message in st.session_state.chat_history:
    if "user" in message:
        st.write(f"You: {message['user']}")
    elif "bot" in message:
        st.write(f"Bot: {message['bot']}")
