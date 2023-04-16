import streamlit as st
from PIL import Image


def main():
    st.title("Intro")
    st.write("")
    # The Poster
    image_0 = Image.open('../images/intro_poster.png')
    st.image(image_0)
    # The Intro
    image_1 = Image.open('../images/intro_intro.png')
    st.image(image_1)
    # Gladiator prediction intro
    image_2 = Image.open('../images/intro_gladiator.png')
    st.image(image_2)

if __name__ == '__main__':
    main()