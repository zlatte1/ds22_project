import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


# Plots text color
params = {"ytick.color" : "w",
          "xtick.color" : "w",
          "axes.labelcolor" : "w",
          "axes.edgecolor" : "w"}
plt.rcParams.update(params)

text_color = 'white'
black_bg = '#0e1116'



def main():
    st.title("EDA")
    st.write("")
    image = Image.open('./images/eda.png')
    st.image(image)

    st.write("")
    st.write("")

    st.markdown("""
    The dataset is heavly categorical therefore some preprocessing was 
    required in order to visualise it.
    """)
    st.write("")

    # DATA
    data = pd.read_csv("./data/movies.csv")
    data_pro = pd.read_csv("./data/new_dataset.csv")


    # CORRELATION MATRIX
    fig, ax = plt.subplots(figsize=(13,11))
    st.header("1. Variable Correlations")
    st.markdown("""
    The dataset shows the strongest correlation for the finance variables, 
    Budget and Income. These are also related to the Action and Animation
    genres due to the high costs of producing these movies. As for the 
    rating, it has the highest relation with Income, drama and bibliographical
    movies.
    """)
    corr_matrix = data_pro.corr()
    sns.heatmap(corr_matrix, cmap='Spectral')
    
    # Display plot
    fig.patch.set_facecolor(black_bg)
    st.pyplot(fig)

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")


    # RATINGS DISTRIBUTION
    st.header("2. Distribution of Movie Ratings")
    st.markdown("""
    The most common rating for the top movies is between 6.5-7.5. It 
    shows that users tend to give 6.5 or 7.5 for an average movie meaning 
    the highly rated movies are expected to have a score of 8 and above.
    """)

    # Create plot
    fig, ax = plt.subplots(figsize=(10,7))

    # Plot
    sns.distplot(data['Rating'], bins=30, kde=True, color='palegreen')
    ax.set_xlabel('Rating', fontsize=15)
    ax.set_ylabel('Density', fontsize=15)
    ax.set_facecolor(black_bg)

    # Table
    col_labels = ['Most Common Scores']
    row_labels = ['1', '2', '3', '4', '5']
    table_vals = [[6.6],[7.1],[7.3],[7.0],[6.5]]
    table = ax.table(cellText=table_vals,
            colLabels=col_labels,
            rowLabels=row_labels,
            loc='right')

    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(0.3, 2)

    # Display plot
    fig.patch.set_facecolor(black_bg)
    st.pyplot(fig)

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")


    # GENRE DISTRIBUTION
    st.header("3. Movie Genres")
    st.markdown("""
    The top genres are Drama, Action, Comedy, and Adventure. Important to
    note that all movie genres are not represented in the dataset but only 20.
    """)

    fig, ax1 = plt.subplots(figsize=(20,8))

    # Selecting the Genre columns
    genre_columns = data_pro.columns[8:27]
    df_pie = data_pro[genre_columns]

    # Pie chart for the genres
    sums = df_pie.sum()
    ax1.pie(sums, labels=sums.index,textprops={'color': text_color}, colors=sns.color_palette('Paired'))

    # Display plot
    fig.patch.set_facecolor(black_bg)
    st.pyplot(fig)


    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")


    # RATINGS DISTRIBUTION
    st.header("4. Budget vs. Profit")
    st.markdown("""
    In summary most movies make more than they spend.  
    """)

    fig, ax = plt.subplots(figsize=(30,15))

    # Line chart for the budget and income
    ax.bar(data_pro['Title'], data_pro['Income'], label='Profit', color='lightblue')
    ax.bar(data_pro['Title'], data_pro['Budget'], label='Budget', color='orange')
    ax.legend(loc='upper right', fontsize=30, facecolor=black_bg, labelcolor=text_color)
    ax.set_facecolor(black_bg)  

    # Display plot
    fig.patch.set_facecolor(black_bg)
    st.pyplot(fig)

if __name__ == '__main__':
    main()