import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import imdb
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


dataset = pd.read_csv('new_dataset.csv')
test_df = dataset.iloc[:20, :]


def get_value(val):
    ''' 
    Converts input string to an integer.
    '''
    # 1. Check if the last character of the string is a k or m and if
    # not it converts the string to an int
    if val[-1].lower() not in ['k', 'K', 'm', 'M']:
        return int(val)
    multiplier = val[-1].lower()
    # 2. If the string ends with K multiply by 1000
    if multiplier == "k" or multiplier == "K":
        value = float(val[:-1]) * 1000
        return value
    # 3. If the string ends with M multiply by 1000000 
    elif multiplier == "m" or multiplier == "M":
        value = float(val[:-1]) * 1000000
        return value

get_value('1k')

# 
def searching_IMDb_movie(title_column, dataset):
    """
    Updating the dataset by adding two new columns including metascore
    and number of ratings.
    
    Parameters:
    name_column : the column containing the person's name
    dataset : dataset
    person_type : must specify for IMDb if person is 'actor'/'director'
    """
    # 1. Instantiating imdb 
    ia = imdb.IMDb()

    # 2. For each row of the df, extract the name for specific column
    for index, row in dataset.iterrows():
        try:
            # Get the movie title
            movie_title = row[title_column]
            
            # Search for a movie by title
            movie = ia.search_movie(movie_title)
            movie_id = movie[0].getID()            

            # Make a GET request to the URL and get the HTML content
            movie_req = Request(
                url = f'https://www.imdb.com/title/tt{movie_id}/', 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            movie_html = urlopen(movie_req).read()
            movie_soup = BeautifulSoup(movie_html, 'html.parser')

            # For metascore
            meta_req = Request(
                url = f'https://www.imdb.com/title/tt{movie_id}/criticreviews/?ref_=tt_ov_rt', 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            meta_html = urlopen(meta_req).read()
            meta_soup = BeautifulSoup(meta_html, 'html.parser')
            # If metascore exists
            try:
                metascore_line = meta_soup.find('div', {'class': 'sc-79ae5a4-0 kUTYKi'}).text.split()
                metascore = get_value(metascore_line[0].split('M')[0])
            except AttributeError:
                metascore = None

            # If number of votes exists
            try:
                num_votes_line = movie_soup.find('div', {'class': 'sc-e457ee34-3 frEfSL'}).text.split()
                num_votes = get_value(num_votes_line[0])
            except AttributeError:
                num_votes = None

        except imdb._exceptions.IMDbError:
            metascore = None
            num_votes = None

        dataset.loc[index, f'{title_column}_metascore'] = metascore
        dataset.loc[index, f'{title_column}_num_votes'] = num_votes
    
        print(index)

#searching_IMDb_movie('Title', test_df)
#print('Hi')


def searching_IMDb_person(name_column, dataset, person_type):
    """
    Updating the dataset by adding new column for a director/actor
    including; number of movies, commulative average rating for these
    movies, number of won awards, number of nominations. 
    
    Parameters:
    name_column : the column containing the person's name
    dataset : dataset
    """
    # 1. Instantiating imdb 
    ia = imdb.IMDb()

    # 2. For each row of the df, extract the name for specific column
    for index, row in dataset.iterrows():
        try:
            name = row[name_column]
            # Fetch the IMDb name results based on the person's name
            name_search = ia.search_person(name)
            person_id = name_search[0].getID()
            
            # Make a GET request to the URL and get the HTML content
            awards_req = Request(
                url = f'https://www.imdb.com/name/nm{person_id}/awards/?ref_=nm_awd', 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            awards_html = urlopen(awards_req).read()
            awards_soup = BeautifulSoup(awards_html, 'html.parser')

            # If metascore exists
            try:
                awards_line = awards_soup.find('div', {'class': 'desc'}).text.split()
                wins = get_value(awards_line[2])
                nominations = get_value(awards_line[5])
            except AttributeError:
                wins = None
                nominations = None

            if person_type == 'director':
                movies_req = Request(
                    url = f'https://www.imdb.com/filmosearch/?explore=title_type&role=nm{person_id}&ref_=filmo_ref_job_typ&sort=release_date,asc&mode=detail&page=1&job_type=director', 
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
            elif person_type == 'actor':
                 movies_req = Request(
                    url = f'https://www.imdb.com/filmosearch/?explore=title_type&role=nm{person_id}&ref_=filmo_ref_job_typ&sort=user_rating,desc&mode=detail&page=1&job_type=actor', 
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
            movie_html = urlopen(movies_req).read()
            movie_soup = BeautifulSoup(movie_html, 'html.parser')

            # If metascore exists
            try:
                movies_list = movie_soup.find_all('div', {'class': 'lister-item mode-detail'})
                ratings_list = []
                for movie in movies_list:
                    year_raw = movie.find('span', {'class': 'lister-item-year'}).text.strip('()')
                    year_match = re.match(r'^\d{4}$', year_raw)
                    if year_match and int(year_raw) < 2023:
                        rating = movie.find('div', {'class': 'ratings-bar'}).find('div', {'class': 'inline-block ratings-imdb-rating'})
                        if rating is not None:
                            ratings_list.append(float(rating['data-value']))
            except AttributeError:
                ratings_list = None

        except imdb._exceptions.IMDbError:
            wins = None
            nominations = None
            ratings_list = None

        dataset.loc[index, f'{name_column}_num_wins'] = wins
        dataset.loc[index, f'{name_column}_num_nominations'] = nominations
        dataset.loc[index, f'{name_column}_num_movies'] = len(ratings_list)
        dataset.loc[index, f'{name_column}_avg_rating'] = np.mean(ratings_list)

        print(index)

    return dataset

searching_IMDb_person('Supporting', test_df, 'actor')


# Function to find number of movies and average rating for person
# def searching_IMDb_person(name_column, dataset, person_type):
#     """
#     Updating the dataset by adding new column for a director/actor
#     including; number of movies, commulative average rating for these
#     movies, number of won awards, number of nominations. 
    
#     Parameters:
#     name_column : the column containing the person's name
#     dataset : dataset
#     person_type : must specify for IMDb if person is 'actor'/'director'
#     """
#     # 1. Instantiating imdb 
#     ia = imdb.IMDb()

#     # 2. For each row of the df, extract the name for specific column
#     for index, row in dataset.iterrows():
#         try:
#             name = row[name_column]
#             # Fetch the IMDb name results based on the person's name
#             name_search = ia.search_person(name)
#             person_id = name_search[0].getID()
            
#             # Make a GET request to the URL and get the HTML content
#             awards_req = Request(
#                 url = f'https://www.imdb.com/name/nm{person_id}/awards/?ref_=nm_awd', 
#                 headers={'User-Agent': 'Mozilla/5.0'}
#             )
#             awards_html = urlopen(awards_req).read()
#             awards_soup = BeautifulSoup(awards_html, 'html.parser')

#             # If metascore exists
#             try:
#                 awards_line = awards_soup.find('div', {'class': 'desc'}).text.split()
#                 wins = get_value(awards_line[2])
#                 nominations = get_value(awards_line[5])
#             except AttributeError:
#                 wins = None
#                 nominations = None

#             # Extract the movies and ratings for the actor        
#             person = ia.get_person(person_id)
#             ia.update(person, 'filmography')
#             ratings_list = []
#             try:
#                 # Iterate over the actor's filmography and extract the movie id
#                 for movie in person['filmography'][person_type]:
#                     movie_title = movie.movieID

#                     # Get the movie's rating based on the movie id
#                     movie = ia.get_movie(movie_title)
#                     release_year = movie.get('year')

#                     # Handle release years
#                     if release_year is not None:
#                         release_year = int(release_year)
#                     else:
#                         release_year = 0

#                     # Keep only ratings with release year up to 2023
#                     rating = movie.get('rating')
#                     if 0 < release_year < 2024 and rating is not None:
#                         ratings_list.append(float(rating))
#             except KeyError:
#                 ratings_list = []

#         except imdb._exceptions.IMDbError:
#             wins = None
#             nominations = None
#             ratings_list = []
        
#         dataset.loc[index, f'{name_column}_num_movies'] = len(ratings_list)
#         dataset.loc[index, f'{name_column}_avg_rating'] = np.mean(ratings_list)
#         dataset.loc[index, f'{name_column}_num_wins'] = wins
#         dataset.loc[index, f'{name_column}_num_nominations'] = nominations

#         print(index)

#     return dataset


#searching_IMDb_person('Supporting', test_df)
#searching_IMDb_person('Director', test_df, 'director')
print('hi')
