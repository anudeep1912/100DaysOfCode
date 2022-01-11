from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

DATE = "2020-12-02"
URL = f"https://www.billboard.com/charts/hot-100/{DATE}/"

# Get the HTML of the Bill board Top - 100 and parse using beautiful soup
response = requests.get(URL)
billboard_html = response.text
soup = BeautifulSoup(billboard_html, "html.parser")

# Extract all the 100 song names from the HTML
song_names = []
first_song = soup.find(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
song_names.append(first_song.getText().strip())
songs = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
for song in songs:
    song_names.append(song.getText().strip())


load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)


user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = DATE.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
