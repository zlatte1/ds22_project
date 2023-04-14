import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Dummy Data
# Load data from CSV file
df = pd.read_csv("./data/data.csv")

# Get list of column names
columns = list(df.columns)

# Select column to plot
selected_column = st.selectbox("Select a column to plot", columns)

# Create plot
fig, ax = plt.subplots()
ax.plot(df[selected_column])

# Display plot







def main():
    st.title("Graph")
    st.pyplot(fig)



if __name__ == '__main__':
    main()