import streamlit as st
import joblib

# Load your pre-trained model
pipeline = joblib.load("svm_model.joblib")

# Function to predict response
def predict_input_svm(pipeline, user_input):
    predicted_response = pipeline.predict([user_input])[0]
    return predicted_response

# Define Streamlit UI
st.title("Mental Healthcare Chatbot")

# Add a text input field for user input
user_input = st.text_input("You:", "")

# Add a button to submit user input
if st.button("Send"):
    # Predict response based on user input
    bot_response = predict_input_svm(pipeline, user_input)
    
    # Display bot response
    st.text_area("Bot:", value=bot_response, height=100)