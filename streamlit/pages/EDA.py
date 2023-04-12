import streamlit as st
from PIL import Image

image = Image.open('imdb.png')

st.image(image, caption='Sunrise by the mountains')
def main():
    st.title("Page2")
    st.write("This is a simple Streamlit app.")
    st.write("Try changing the value of the slider below:")
    x = st.slider('x', 0, 100, 50)
    st.write('The value of x is:', x)

if __name__ == '__main__':
    main()