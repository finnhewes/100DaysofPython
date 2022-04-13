import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# As these are personal account details, I've set them as environment variables. You'll need to establish your own
# spotify developer account and input these details to try out this code, which can be done for free
# follow this link to get started >>> https://developer.spotify.com/dashboard/

spotify_client_id = os.environ["SPOTIFY_CLIENT_ID"]
spotify_client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]

# Taking user date input to create a playlist from
user_input = input("Which date shall we search? Please enter in the YYYY-MM-DD format:\n")

#   Scraping billboard.com for top 100 charts for user inputted date
billboard_data = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input}/")
billboard_html_content = billboard_data.text
soup = BeautifulSoup(billboard_html_content, "html.parser")

#    Separate song titles from soup
temp_s_list = []
song_titles = soup.find_all(name="h3", class_="a-font-primary-bold-s")
for song in song_titles:
    txt = song.getText()
    x = txt.strip("\n\t")
    temp_s_list.append(x)
titles_list = temp_s_list[2:]

#    Separate artists' names from soup
artists_list = []
artists = soup.select("span.c-label.a-no-trucate.a-font-primary-s")
for artist in artists:
    txt = artist.getText()
    x = txt.strip("\n\t")
    artists_list.append(x)

#   Spotify OAuth and Client requests below
sp = spotipy.oauth2.SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri="http://example.com", state=None, scope="playlist-modify-private", cache_path=None, username="31ou36admfffszhdj6ymgc72ko7q", proxies=None, show_dialog=False, requests_session=True, requests_timeout=None)
cl = spotipy.client.Spotify(auth=None, requests_session=True, client_credentials_manager=None, oauth_manager=sp, auth_manager=None, proxies=None, requests_timeout=5, status_forcelist=None, retries=3, status_retries=3, backoff_factor=0.3)
user_id = cl.current_user()["id"]

#   searching Spotify for the uri's of all the songs we generated above, and adding them to a URI list (if available).
uri_list = []
for each in titles_list:
    ind = titles_list.index(each)
    artist = artists_list[ind]
    # using both song name and artist name in our query, which supposedly yields results with about 99% accuracy
    query = each + " " + artist
    searchResults = cl.search(q=query, market="US", limit=1)
    try:
        uri=(searchResults["tracks"]["items"][0]["uri"])
        uri_list.append(uri)
    #   If the song is NOT available, they will be skipped over
    except IndexError:
        pass

#   Adding all the songs in the uri_list above to a newly generated spotify playlist named after the user input above
pl = cl.user_playlist_create(user_id, name=f"{user_input} Billboard 100", public=False, description=f"A playlist of the available songs from the Billboard Top 100 list from the date {user_input}.")
playlist_uri = pl["uri"]
cl.playlist_add_items(playlist_uri, uri_list)

# sample input:    2010-08-12
