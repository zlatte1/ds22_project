import streamlit as st

def main():
    st.title("Hello, World!")
    st.write("This is a simple Streamlit app.")
    st.write("Try changing the value of the slider below:")
    x = st.slider('x', 0, 100, 50)
    st.write('The value of x is:', x)

if __name__ == '__main__':
    main()
