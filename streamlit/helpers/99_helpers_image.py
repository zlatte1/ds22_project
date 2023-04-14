import streamlit as st

#import and dislplay image
from PIL import Image
image = Image.open('./images/imdb.png')
st.image(image, caption='Sunrise by the mountains')

def main():
    st.title("How to import Image")
    st.write("")

if __name__ == '__main__':
    main()