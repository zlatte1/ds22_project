import streamlit as st
from PIL import Image

def main():
    st.title("Conclusion")
    st.write("ThougtS:")
    st.write("Limitaton of the model:")
    st.write("Basically since the dataset is top100 movies from the last 20y, its going to be able to predict blockbusters pretty well but not horror, doc, bollywood or foreign")
    st.write("What would we do if we had more time and resources")
    st.write("scrape all movies on imdb and maybe even add a second source of data -- RT")
    st.write("Data-nice-to-have:")
    st.write("film_company:")
    st.write("ThougtS:")
    st.write("out of a buisness/ client perspective it would make more sense to predict income or ROI ")
    st.write("and what features has the highest co-eff to this")

    image_0 = Image.open('./images/conclusion_pred.png')
    st.image(image_0)
if __name__ == '__main__':
    main()