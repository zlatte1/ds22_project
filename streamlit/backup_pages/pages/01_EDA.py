import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("./data/movies.csv")

# Get number of rows and columns
num_rows, num_cols = df.shape

#create col for rows and columns
data_col_rows = [["Columns", num_cols],
        ["Row", num_rows]]

df_col_rows = pd.DataFrame(data_col_rows)

col_types = df.dtypes

def main():
    st.title("EDA")
    st.write(df.head())



# Display the DataFrame
    st.write("Total number of columns and rows")
    st.write(df_col_rows)

    st.write("Type of columns")
    st.write(col_types)
    
    st.write("check for null values in all columns")
    st.write(df.isnull().sum())

if __name__ == '__main__':
    main()