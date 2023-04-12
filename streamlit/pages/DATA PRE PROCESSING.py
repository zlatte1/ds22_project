import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")




def main():
    st.title("Graph")
    st.write(df.head())


if __name__ == '__main__':
    main()