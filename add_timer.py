import streamlit as st
import time
import random

# Initialize session state variables
if 'seconds_left' not in st.session_state:
    st.session_state.seconds_left = 60  # Timer set to 60 seconds

if 'random_numbers' not in st.session_state:
    st.session_state.random_numbers = (random.randint(2, 9), random.randint(2, 9))

if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = 0

if 'incorrect_answers' not in st.session_state:
    st.session_state.incorrect_answers = 0

def decrement_timer():
    if st.session_state.seconds_left > 0:
        st.session_state.seconds_left -= 1

# Display the timer
st.title("60-Second Math Challenge")

# Show the current timer value
timer_display = st.empty()
timer_display.write(f"Time left: {st.session_state.seconds_left} seconds")

# Generate two random numbers
num1, num2 = st.session_state.random_numbers
correct_sum = num1 + num2

# Display random numbers and get the user's answer
st.write(f"What's the sum of {num1} + {num2}?")
options = list(range(0, 19))  # Possible sums of two numbers between 0 and 9
user_answer = st.selectbox("Select the sum:", options)

# Check user's answer when the dropdown value changes
submit_button = st.button("Submit Answer", disabled=st.session_state.seconds_left == 0)
if submit_button:
    if user_answer == correct_sum:
        st.session_state.correct_answers += 1
    else:
        st.session_state.incorrect_answers += 1
    # Generate new random numbers for the next round
    st.session_state.random_numbers = (random.randint(0, 9), random.randint(0, 9))

# Display the number of correct and incorrect answers
st.write(f"Correct Answers: {st.session_state.correct_answers}")
st.write(f"Incorrect Answers: {st.session_state.incorrect_answers}")

# Timer logic
if st.session_state.seconds_left > 0:
    time.sleep(1)
    decrement_timer()
    st.experimental_rerun()
else:
    st.write("Timer has finished! No more actions can be performed.")
