import streamlit as st
import pickle 
import pandas as pd
import requests
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

movies_df = pickle.load(open('movies.pkl','rb'))
movies = movies_df[['title']]
movie_titles = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))


def fetch_poster(m_id):
    
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(m_id)
   
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('TMDB_BEARER_TOKEN')}"
    }   
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']
    
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]].movie_id 
        
        recommended_movies.append(movies.iloc[i[0]]['title'])
        
        #Fetching poster from api using tmdb id
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select Your Movie Of Liking', movie_titles)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    
    col = st.columns(5)

    for i in range(0,5):
        
        with col[i]:
            st.text(names[i])
            st.image(posters[i])

    