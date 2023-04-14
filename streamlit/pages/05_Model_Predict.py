import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import time

#Load model, Should change to the best performing later on.
model_rf = joblib.load("./models/model_rf.joblib")
model_dt = joblib.load("./models/model_dt_vot.joblib")

# Display input form
st.subheader("Fill in form or choose one of the pre-programmed to the left")

# Year, month, and runtime inputs
year, month, runtime = st.columns(3)
year = year.number_input("Year (1950-2023)", value=2012, min_value=1950, max_value=2023)
month = month.number_input("Month (Jan = 1 .. Dec = 12)", value=7, min_value=1, max_value=12)
runtime = runtime.number_input("Runtime (min)", value=111, min_value=20, max_value=400)


income, budget = st.columns(2)
income = income.number_input("Income ($)", value=121468526, min_value=0)
budget = budget.number_input("Budget ($)", value=44189775, min_value=0)

s1_top1000, s2_top1000, s3_top1000, s4_top1000 = st.columns(4)
s1_top1000 = s1_top1000.number_input("Star1_top1000 (0/1)", value=0, min_value=0, max_value=1)
s2_top1000 = s2_top1000.number_input("Star2_top1000 (0/1)", value=0, min_value=0, max_value=1)    
s3_top1000 = s3_top1000.number_input("Star3_top1000 (0/1)", value=0, min_value=0, max_value=1)    
s4_top1000 = s4_top1000.number_input("Star4_top1000 (0/1)", value=0, min_value=0, max_value=1)

d1_top50, d2_top50 = st.columns(2)
d1_top50 = d1_top50.number_input("Director1_top50 (0/1)", value=0, min_value=0, max_value=1)
d2_top50 = d2_top50.number_input("Director2_top50 (0/1)", value=0, min_value=0, max_value=1)

# Genre options
genre_options = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
selected_genres = st.multiselect("Genre(s)", genre_options, default=['Action'])

# Create variables for each genre option
genre_Action = 1 if 'Action' in selected_genres else 0
genre_Adventure = 1 if 'Adventure' in selected_genres else 0
genre_Animation = 1 if 'Animation' in selected_genres else 0
genre_Biography = 1 if 'Biography' in selected_genres else 0
genre_Comedy = 1 if 'Comedy' in selected_genres else 0
genre_Crime = 1 if 'Crime' in selected_genres else 0
genre_Drama = 1 if 'Drama' in selected_genres else 0
genre_Family = 1 if 'Family' in selected_genres else 0
genre_Fantasy = 1 if 'Fantasy' in selected_genres else 0
genre_History = 1 if 'History' in selected_genres else 0
genre_Horror = 1 if 'Horror' in selected_genres else 0
genre_Music = 1 if 'Music' in selected_genres else 0
genre_Musical = 1 if 'Musical' in selected_genres else 0
genre_Mystery = 1 if 'Mystery' in selected_genres else 0
genre_Romance = 1 if 'Romance' in selected_genres else 0
genre_SciFi = 1 if 'Sci-Fi' in selected_genres else 0
genre_Sport = 1 if 'Sport' in selected_genres else 0
genre_Thriller = 1 if 'Thriller' in selected_genres else 0
genre_War = 1 if 'War' in selected_genres else 0
genre_Western = 1 if 'Western' in selected_genres else 0




cert_options = ['G', 'NC-17', 'PG', 'PG-13', 'R', 'TV-14', 'TV-G', 'TV-MA', 'TV-PG', 'TV-Y7']
cert = st.selectbox("Certificate", cert_options)

# Create variables for each certificate option
cert_G = 1 if cert == 'G' else 0
cert_NC_17 = 1 if cert == 'NC-17' else 0
cert_PG = 1 if cert == 'PG' else 0
cert_PG_13 = 1 if cert == 'PG-13' else 0
cert_R = 1 if cert == 'R' else 0
cert_TV_14 = 1 if cert == 'TV-14' else 0
cert_TV_G = 1 if cert == 'TV-G' else 0
cert_TV_MA = 1 if cert == 'TV-MA' else 0
cert_TV_PG = 1 if cert == 'TV-PG' else 0
cert_TV_Y7 = 1 if cert == 'TV-Y7' else 0


# Continent options
continent_options = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
selected_continents = st.multiselect("Continent(s) of Origin", continent_options, default=['North America'])

# Create variables for each continent option
continent_Africa = 1 if 'Africa' in selected_continents else 0
continent_Asia = 1 if 'Asia' in selected_continents else 0
continent_Europe = 1 if 'Europe' in selected_continents else 0
continent_North_America = 1 if 'North America' in selected_continents else 0
continent_Oceania = 1 if 'Oceania' in selected_continents else 0
continent_South_America = 1 if 'South America' in selected_continents else 0






# calculate profit and difference between income and budget
profit = income - budget

# calculate ROI based on user input
roi = (profit / budget) * 100








def make_prediction(year, month, runtime, cert_G, cert_NC_17, cert_PG, cert_PG_13, cert_R, cert_TV_14, cert_TV_G, cert_TV_MA, cert_TV_PG, cert_TV_Y7, d1_top50, d2_top50, s1_top1000, s2_top1000, s3_top1000, s4_top1000, genre_Action, genre_Adventure, genre_Animation, genre_Biography, genre_Comedy, genre_Crime, genre_Drama, genre_Family, genre_Fantasy, genre_History, genre_Horror, genre_Music, genre_Musical, genre_Mystery, genre_Romance, genre_SciFi, genre_Sport, genre_Thriller, genre_War, genre_Western, continent_Africa, continent_Asia, continent_Europe, continent_North_America, continent_Oceania, continent_South_America, budget, income, profit, roi):

    with st.spinner('Predicting...'):
    # Delay
        time.sleep(5)

        # Make prediction
        prediction_rf = model_rf.predict([[year, month, runtime, cert_G, cert_NC_17, cert_PG, cert_PG_13, cert_R, cert_TV_14, cert_TV_G, cert_TV_MA, cert_TV_PG, cert_TV_Y7 , d1_top50, d2_top50, s1_top1000, s2_top1000, s3_top1000, s4_top1000, genre_Action, genre_Adventure, genre_Animation, genre_Biography, genre_Comedy, genre_Crime, genre_Drama, genre_Family, genre_Fantasy, genre_History, genre_Horror, genre_Music, genre_Musical, genre_Mystery, genre_Romance, genre_SciFi, genre_Sport, genre_Thriller, genre_War, genre_Western, continent_Africa, continent_Asia, continent_Europe, continent_North_America, continent_Oceania, continent_South_America, budget, income, profit, roi]])
        prediction_dt = model_dt.predict([[year, month, runtime, cert_G, cert_NC_17, cert_PG, cert_PG_13, cert_R, cert_TV_14, cert_TV_G, cert_TV_MA, cert_TV_PG, cert_TV_Y7 , d1_top50, d2_top50, s1_top1000, s2_top1000, s3_top1000, s4_top1000, genre_Action, genre_Adventure, genre_Animation, genre_Biography, genre_Comedy, genre_Crime, genre_Drama, genre_Family, genre_Fantasy, genre_History, genre_Horror, genre_Music, genre_Musical, genre_Mystery, genre_Romance, genre_SciFi, genre_Sport, genre_Thriller, genre_War, genre_Western, continent_Africa, continent_Asia, continent_Europe, continent_North_America, continent_Oceania, continent_South_America, budget, income, profit, roi]])

        # Remove the spinner animation and display the prediction results

        data = {
            "Model": ["Random Forest", "Decision Tree Voting"],
            "Rating": [prediction_rf[0], prediction_dt[0]]
        }
        df = pd.DataFrame(data, index=None)
        df["Rating"] = df["Rating"].round(1)

        st.write(df)


#make_prediction(year, month, runtime, cert_G, cert_NC_17, cert_PG, cert_PG_13, cert_R, cert_TV_14, cert_TV_G, cert_TV_MA, cert_TV_PG, cert_TV_Y7 , d1_top50, d2_top50, s1_top1000, s2_top1000, s3_top1000, s4_top1000, genre_Action, genre_Adventure, genre_Animation, genre_Biography, genre_Comedy, genre_Crime, genre_Drama, genre_Family, genre_Fantasy, genre_History, genre_Horror, genre_Music, genre_Musical, genre_Mystery, genre_Romance, genre_SciFi, genre_Sport, genre_Thriller, genre_War, genre_Western, continent_Africa, continent_Asia, continent_Europe, continent_North_America, continent_Oceania, continent_South_America, budget, income, profit, roi)


# Define the initial movie selection and movie names list
# Define the initial movie selection and movie names list
#movie_select = "Select a movie..."
# Define the initial movie selection and movie names list
# Define the initial movie selection and movie names list
movie_names = ["The Shawshank Redemption",  "Gladiator", "Gladiator 2", "A Man Called Otto"]
movie_select = None

# Add the movie buttons and update the selected movie dynamically
st.sidebar.write("Select a movie:")
for movie_name in movie_names:
    if st.sidebar.button(movie_name):
        movie_select = movie_name

# Check if a movie has been selected
if movie_select:
    if movie_select == "The Shawshank Redemption":
        budget = 25000000
        income = 28767189
        profit = income - budget
        roi = profit / budget
        make_prediction(1994, 10, 142, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 , 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, budget, income, profit, roi)
    elif movie_select == "Gladiator":
        budget = 103000000
        income = 187705427
        profit = income - budget
        roi = profit / budget
        make_prediction(2000, 5, 155, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 , 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, budget, income, profit, roi)
    elif movie_select == "Gladiator 2":
        budget = 71491880
        roi = 0.6490
        income = budget * (1 + roi)
        profit = income - budget
        make_prediction(2023, 11, 111, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 , 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, budget, income, profit, roi)
    elif movie_select == "A Man Called Otto":
        budget = 50000000
        income = 64263300
        profit = income - budget
        roi = profit / budget
        make_prediction(2022, 1, 126, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 , 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, budget, income, profit, roi)

    else:
        st.sidebar.write("Invalid movie selection")
else:
    st.sidebar.write("")




# Display the selected movie in the sidebar
#st.sidebar.write("Selected movie:", movie_select)



def main():
    # -st.title("Graph")
    #st.write(df.head())
    # Display prediction
    if st.button("Predict", key="predict_button"):
        #st.write(movie_select)
        # Display the spinner animation
        make_prediction(year, month, runtime, cert_G, cert_NC_17, cert_PG, cert_PG_13, cert_R, cert_TV_14, cert_TV_G, cert_TV_MA, cert_TV_PG, cert_TV_Y7 , d1_top50, d2_top50, s1_top1000, s2_top1000, s3_top1000, s4_top1000, genre_Action, genre_Adventure, genre_Animation, genre_Biography, genre_Comedy, genre_Crime, genre_Drama, genre_Family, genre_Fantasy, genre_History, genre_Horror, genre_Music, genre_Musical, genre_Mystery, genre_Romance, genre_SciFi, genre_Sport, genre_Thriller, genre_War, genre_Western, continent_Africa, continent_Asia, continent_Europe, continent_North_America, continent_Oceania, continent_South_America, budget, income, profit, roi)





if __name__ == '__main__':
    main()