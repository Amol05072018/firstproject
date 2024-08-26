import streamlit as st
import random

# Function to generate two random single-digit integers
def generate_numbers():
    return random.randint(1, 9), random.randint(1, 9)

# Initialize session state for the numbers and counters
if 'num1' not in st.session_state or 'num2' not in st.session_state:
    st.session_state.num1, st.session_state.num2 = generate_numbers()
if 'correct_count' not in st.session_state:
    st.session_state.correct_count = 0
if 'incorrect_count' not in st.session_state:
    st.session_state.incorrect_count = 0
if 'user_sum' not in st.session_state:
    st.session_state.user_sum = 0

# Retrieve stored numbers and user input
num1 = st.session_state.num1
num2 = st.session_state.num2

st.title("Simple Addition App")

# Display the numbers to be added
question_text = f"Add the following numbers: {num1} + {num2}"
st.write(question_text)

# User input for the sum using dropdown menu
options = list(range(19))  # Options from 0 to 18
user_sum = st.selectbox("Select your answer", options, key='user_sum_select')

# Check if the user has submitted an answer
if st.button("Submit"):
    correct_answer = num1 + num2
    if user_sum == correct_answer:
        st.success("Good Job!")
        st.session_state.correct_count += 1
    else:
        st.error("Wrong Answer")
        st.session_state.incorrect_count += 1

    # Generate new numbers for the next question
    st.session_state.num1, st.session_state.num2 = generate_numbers()

    # Reset user input (selectbox does not need explicit reset, but it's kept here for clarity)
    st.session_state.user_sum = 0

    # Refresh the display to show new numbers
    st.experimental_rerun()

# Display the counters for correct and incorrect answers
st.write(f"Correct Answers: {st.session_state.correct_count}")
st.write(f"Incorrect Answers: {st.session_state.incorrect_count}")

# Check if the user has reached 30 correct answers
if st.session_state.correct_count >= 30:
    st.balloons()  # Optional: Show some celebration balloons
    st.success("Congratulations! Level Completed.")
else:
    st.warning("Close Browser and Try Again.")
