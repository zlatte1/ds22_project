import streamlit as st
from PIL import Image
image = Image.open('./images/model_dev_01.png')


list_of_bullets = [
    '- Models applied initially : Linear regression, polynomial regression, KNN, SVR, DT, For., Lasso regression, Ensemble models (voting and bagging regressor) and Neural network (keras)',
    '- Scaled on RobustScaler for optimal coefficients and have better performance',
    '- checked: performance metrics of R2, RMSE, mse, mae'
]

def main():
    st.title("Model Development")
    for item in list_of_bullets:
        st.write(item)

    st.subheader("Here are initial results of ML models:")
    st.image(image, caption='')

if __name__ == '__main__':
    main()