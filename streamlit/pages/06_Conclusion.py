import streamlit as st
from PIL import Image

def main():
    st.title("Conclusion")
 
    image_0 = Image.open('../images/conclusion_pred.png')
    st.image(image_0)

    st.subheader("Purpose")
    st.write("Using Machine Learning to Predict Movie Ratings")

    st.subheader("How did we do?")
    st.write("-- Perfomance Metrics/ Models")
    st.write("-- Limitations")
    st.write("-- What would we do diffrently")

    st.write("Summarize what the product actually do")

if __name__ == '__main__':
    main()