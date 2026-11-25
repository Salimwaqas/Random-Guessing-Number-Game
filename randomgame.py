import streamlit as st
st.title("Random Guessing Number Game")
secret=5
number1=st.number_input("Write a number between 1-10")
if st.button("Submit"):
    if number1 == secret:
        st.success("Correct")
    else:
        st.warning("Wrong Number")