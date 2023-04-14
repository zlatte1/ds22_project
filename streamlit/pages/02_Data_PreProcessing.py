import streamlit as st
from PIL import Image


def main():
    st.title("Data Pre Processing")
    st.write("")
    st.markdown("""
    The dataset requires processing and feature engineering before
    any model training can be done. Almost all variables need to be edited
    but the major problems with the data are:
    """)

    st.write("")
    st.subheader("1. The Genres")
    image_0 = Image.open('./images/processing_genre.png')
    st.image(image_0)

    st.write("")
    st.subheader("2. The Finance Variables")
    image_1 = Image.open('./images/processing_finance.png')
    st.image(image_1)

    st.write("")
    st.subheader("3. The People in the Movies")
    image_2 = Image.open('./images/processing_people.png')
    st.image(image_2)

    st.write("")
    st.subheader("4. The People in the Movies")
    image_3 = Image.open('./images/processing_summary.png')
    st.image(image_3)
    
if __name__ == '__main__':
    main()