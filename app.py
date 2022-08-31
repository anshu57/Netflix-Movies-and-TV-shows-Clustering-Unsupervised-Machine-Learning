from typing import Any

import streamlit as st
import pickle
import pandas as pd


def recomened(show):
    show_index = shows[shows['title'] == show].index[0]
    distances = similarity[show_index]
    shows_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommened_shows = []
    for i in shows_list:
        recommened_shows.append(shows.iloc[i[0]].title)
    return recommened_shows


shows_dict = pickle.load(open('shows_dict.pkl', 'rb'))
shows = pd.DataFrame(shows_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.header('Deployed by Anshu Gangwar')
st.title('Netflix Movies and Shows Recommender System')
selected_show_name = st.selectbox(
    'Select the movie or show to display top 5 recommendations',
    shows['title'].values)
if st.button('Recommened'):
    recommendations = recomened(selected_show_name)
    for i in recommendations:
        st.write(i)
