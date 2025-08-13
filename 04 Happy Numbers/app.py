import streamlit as st
from run import is_happy
from nltk.corpus import words
import nltk

nltk.download('words')

st.title("Happy Numbers")
st.image('./banner.png')

option = st.radio("Featurs :","input happy numbers")

if option == "input happy numbers" :
    is_happy_obj = st.number_input("enter your number")
    if st.button("Check your number"):
        result = is_happy(int(is_happy_obj))
        st.success("the status Your number is:")
        if result :
            st.markdown("your number is **happy**")
            st.image('./happy.png')
        else :
            st.markdown("your number is **sad**") 
            st.image('./sad.png')