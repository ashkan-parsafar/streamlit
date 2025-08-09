import streamlit as st
from generator import generate_random_password, generate_memorable_password, generate_pin
from nltk.corpus import words
import nltk

nltk.download('words')

st.image('./banner.jpeg')
st.title("Password Generator")
st.title("Ashkan")
st.button("Click",type)
st.text("Hello World!")

st.markdown(
    """
    <style>
        .stApp, html, body, [class*="css"] {
            background-color: black !important;
            color: #00FF00 !important;
        }

        label, span, div, p {
            color: #00FF00 !important;
            opacity: 1 !important;
        }

        div[data-baseweb="checkbox"] span, div[data-baseweb="radio"] span {
            color: #00FF00 !important;
            opacity: 1 !important;
        }

        input, textarea {
            color: black !important;
            background-color: white !important;
        }

        .stButton>button {
            background-color: #111 !important;
            color: #00FF00 !important;
            border: 1px solid #00FF00 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


option = st.radio("Password Type:", ('Random Password', 'Memorable Password', 'Pin Code'))

if option == "Random Password":
    length = st.slider("Length", min_value=5, max_value=50, value=5)
    include_numbers = st.checkbox("Include Number")
    include_symbols = st.checkbox("Include Symbols")

    if st.button("Generate Random Password"):
        password = generate_random_password(length, include_numbers, include_symbols)
        st.success("Your password is:")
        st.code(password)

elif option == "Memorable Password":
    vocabulary_items = st.text_input("Enter your words (comma separated):")
    no_of_words = st.slider("Number of Words", min_value=2, max_value=4, value=3)
    separator = st.text_input("Separator", value="-")
    capitalization = st.checkbox("Capitalization")

    if st.button("Generate Memorable Password"):
        if vocabulary_items:
            vocabulary = [item.strip() for item in vocabulary_items.split(',') if item.strip()]
            try:
                password = generate_memorable_password(
                    no_of_words=no_of_words,
                    separator=separator,
                    capitalization=capitalization,
                    vocabulary=vocabulary
                )
                st.success(f"Your password: {password}")
            except ValueError as e:
                st.error(str(e))
        else:
            st.warning("Please enter some words.")

elif option == "Pin Code":
    pin_length = st.slider("PIN Length", min_value=3, max_value=10, value=4)

    if st.button("Generate PIN Code"):
        password = generate_pin(length=pin_length)
        st.success("Your PIN code is:")
        st.code(password)


if 'password' in locals():
    st.write("Your password is:")
    st.header(fr"```{password}```")
