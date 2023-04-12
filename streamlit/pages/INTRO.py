import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

model = joblib.load("model_rf.joblib")

option = st.sidebar.selectbox("Select an option", ["Load Model"])

if option == "Load Model":
    st.write("Model loaded successfully!")

    # Display input form
    st.subheader("Enter Movie-details to get pred Rating")
    year = st.number_input("Year (1900-2023)", value=2023, min_value=1900, max_value=2023)
    month = st.number_input("Month (1-12)", value=1, min_value=1, max_value=12)
    runtime = st.number_input("Runtime (20-400)", value=120, min_value=20, max_value=400)
    
    # Genre options
    genre_options = ['genre_Action', 'genre_Adventure', 'genre_Animation', 'genre_Biography', 'genre_Comedy', 'genre_Crime', 'genre_Drama', 'genre_Family', 'genre_Fantasy', 'genre_History', 'genre_Horror', 'genre_Music', 'genre_Musical', 'genre_Mystery', 'genre_Romance', 'genre_Sci-Fi', 'genre_Sport', 'genre_Thriller', 'genre_War', 'genre_Western']
    selected_genres = st.multiselect("Select Genre(s)", genre_options)

    # Create variables for each genre option
    genre_Action = 1 if 'genre_Action' in selected_genres else 0
    genre_Adventure = 1 if 'genre_Adventure' in selected_genres else 0
    genre_Animation = 1 if 'genre_Animation' in selected_genres else 0
    genre_Biography = 1 if 'genre_Biography' in selected_genres else 0
    genre_Comedy = 1 if 'genre_Comedy' in selected_genres else 0
    genre_Crime = 1 if 'genre_Crime' in selected_genres else 0
    genre_Drama = 1 if 'genre_Drama' in selected_genres else 0
    genre_Family = 1 if 'genre_Family' in selected_genres else 0
    genre_Fantasy = 1 if 'genre_Fantasy' in selected_genres else 0
    genre_History = 1 if 'genre_History' in selected_genres else 0
    genre_Horror = 1 if 'genre_Horror' in selected_genres else 0
    genre_Music = 1 if 'genre_Music' in selected_genres else 0
    genre_Musical = 1 if 'genre_Musical' in selected_genres else 0
    genre_Mystery = 1 if 'genre_Mystery' in selected_genres else 0
    genre_Romance = 1 if 'genre_Romance' in selected_genres else 0
    genre_SciFi = 1 if 'genre_Sci-Fi' in selected_genres else 0
    genre_Sport = 1 if 'genre_Sport' in selected_genres else 0
    genre_Thriller = 1 if 'genre_Thriller' in selected_genres else 0
    genre_War = 1 if 'genre_War' in selected_genres else 0
    genre_Western = 1 if 'genre_Western' in selected_genres else 0

    cert_options = ['cert_G', 'cert_NC-17', 'cert_PG', 'cert_PG-13', 'cert_R', 'cert_TV-14', 'cert_TV-G', 'cert_TV-MA', 'cert_TV-PG', 'cert_TV-Y7']
    cert = st.selectbox("Select Certificate", cert_options)

    # Create variables for each certificate option
    cert_G = 1 if cert == 'cert_G' else 0
    cert_NC_17 = 1 if cert == 'cert_NC-17' else 0
    cert_PG = 1 if cert == 'cert_PG' else 0
    cert_PG_13 = 1 if cert == 'cert_PG-13' else 0
    cert_R = 1 if cert == 'cert_R' else 0
    cert_TV_14 = 1 if cert == 'cert_TV-14' else 0
    cert_TV_G = 1 if cert == 'cert_TV-G' else 0
    cert_TV_MA = 1 if cert == 'cert_TV-MA' else 0
    cert_TV_PG = 1 if cert == 'cert_TV-PG' else 0
    cert_TV_Y7 = 1 if cert == 'cert_TV-Y7' else 0

    # Continent options
    continent_options = ['continent_Africa', 'continent_Asia', 'continent_Europe', 'continent_North America', 'continent_Oceania', 'continent_South America']
    selected_continents = st.multiselect("Select Continent(s)", continent_options)

    # Create variables for each continent option
    continent_Africa = 1 if 'continent_Africa' in selected_continents else 0
    continent_Asia = 1 if 'continent_Asia' in selected_continents else 0
    continent_Europe = 1 if 'continent_Europe' in selected_continents else 0
    continent_North_America = 1 if 'continent_North America' in selected_continents else 0
    continent_Oceania = 1 if 'continent_Oceania' in selected_continents else 0
    continent_South_America = 1 if 'continent_South America' in selected_continents else 0


    d1_top50 = st.number_input("D1_top50 (0/1)", value=0, min_value=0, max_value=1)
    d2_top50 = st.number_input("D2_top50 (0/1)", value=0, min_value=0, max_value=1)
    s1_top1000 = st.number_input("S1_top1000 (0/1)", value=0, min_value=0, max_value=1)
    s2_top1000 = st.number_input("S2_top1000 (0/1)", value=0, min_value=0, max_value=1)    
    s3_top1000 = st.number_input("S3_top1000 (0/1)", value=0, min_value=0, max_value=1)    
    s4_top1000 = st.number_input("S4_top1000 (0/1)", value=0, min_value=0, max_value=1)

    budget = st.number_input("Budget", value=10000, min_value=0, max_value=1000000000000)
    income = st.number_input("Income", value=10000, min_value=0, max_value=1000000000000)
    profit = st.number_input("Profit", value=10000, min_value=0, max_value=1000000000000)
    roi = st.number_input("ROI", value=0.60)

    # Make prediction
    prediction = model.predict([[year, month, runtime, cert_G, cert_NC_17, cert_PG, cert_PG-13, cert_R, cert_TV_14, cert_TV_G, cert_TV_MA, cert_TV_PG, cert_TV_Y7 , d1_top50, d2_top50, s1_top1000, s2_top1000, s3_top1000, s4_top1000, genre_Action, genre_Adventure, genre_Animation, genre_Biography, genre_Comedy, genre_Crime, genre_Drama, genre_Family, genre_Fantasy, genre_History, genre_Horror, genre_Music, genre_Musical, genre_Mystery, genre_Romance, genre_SciFi, genre_Sport, genre_Thriller, genre_War, genre_Western, continent_Africa, continent_Asia, continent_Europe, continent_North_America, continent_Oceania, continent_South_America, budget, income, profit, roi]])


    




# Load data
#df = pd.read_csv("data.csv")




def main():
    # -st.title("Graph")
    #st.write(df.head())
    # Display prediction
    st.subheader("Prediction")
    st.write(f"The estimated Rating of the movies is {prediction[0]:,.2f}")


if __name__ == '__main__':
    main()