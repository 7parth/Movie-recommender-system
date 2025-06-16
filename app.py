import streamlit as st
import pickle 
import pandas as pd

movies_df = pickle.load(open('movies.pkl','rb'))
movies = movies_df[['title']]
movie_titles = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]['title'])
    return recommended_movies

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select Your Movie Of Liking', movie_titles)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
