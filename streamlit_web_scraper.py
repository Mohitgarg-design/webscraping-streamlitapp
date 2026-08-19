import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("🎮 Steam Game Searcher")

game = st.text_input("Enter a game name:")

if st.button("Search"):
    url = "https://store.steampowered.com/search/?term=" + game.replace(" ", "+")

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    games = soup.find_all("span", class_="title")

    if games:
        st.subheader("Search Results")

        for item in games[:10]:
            st.write("🎮", item.text)
    else:
        st.write("No games found.")