import streamlit as st
from PIL import Image
image = Image.open('./images/model_dev_02.png')
image_02 = Image.open('./images/model_dev_03.png')
image_03 = Image.open('./images/model_dev_04.png')



def main():
    st.title("Model Evalulation")
    st.write("Models hypertuned after Grid search & performance metrics")
    st.image(image, caption='')

    st.subheader("Plotting train, test val splits")
    st.write("Polynomial regressor")
    st.image(image_02, caption='')

    st.write("Polynomial regressor visuals")
    st.image(image_03, caption='')

if __name__ == '__main__':
    main()