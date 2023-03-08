from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth




url = "https://www.billboard.com/charts/hot-100/"

date = str(input("Which year? YYYY-MM-DD : "))

response = requests.get(url=f"{url}{date}")
billboard100_page = response.text

soup = BeautifulSoup(billboard100_page, "html.parser")
list = soup.find_all(name="ul", class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")

title_list = []
musician_list = []

for data in list:
    title_list.append(data.find_next(name="h3").getText().strip())
    musician_list.append(data.find_next(name="span").getText().strip())










client_id = ""
client_secret = ""

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="http://example.com", cache_path="token.txt", scope="playlist-modify-private"))

user = sp.current_user()
user_id = user["id"]
username = user["display_name"]
playlist_name = f"{date} billboard 100"

song_uri_list = []

for title in title_list:
    results = sp.search(q=f"track: {title} year:2023", type="track")

    try:
        # musician_name = results["tracks"]["items"][0]["album"]["artists"][0]["name"]
        uri = results["tracks"]["items"][0]["uri"]
        # song_uri_list.append(uri.split(":")[2])
        song_uri_list.append(uri)
    except IndexError:
        print(f"{title} does not exist in spotify.")


response_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
my_playlist_id = response_playlist["id"]

my_playlist = sp.user_playlists(user=user_id)

sp.playlist_add_items(playlist_id=my_playlist_id, items=song_uri_list)








