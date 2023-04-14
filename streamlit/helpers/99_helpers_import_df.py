import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("./data/data.csv")




def main():
    st.title("Load data from df")
    st.write(df.head())


if __name__ == '__main__':
    main()