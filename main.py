import random
from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from playsound import playsound

client_credentials_manager = SpotifyClientCredentials(getenv('SPOTIPY_CLIENT_ID'), getenv('SPOTIPY_CLIENT_SECRET'))
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_artist(name):
  """ get top artist results from search of name """
  results = sp.search(q='artist:' + name, type='artist')
  items = results['artists']['items']
  if len(items) > 0:
    return items[0]
  else:
    return None


def recommend_song(artist):
  """ recommends a song related to artist """
  albums = []
  results = sp.recommendations(seed_artists=[artist['id']], limit=20)
  return random.choice(results['tracks'])


if __name__ == '__main__':
  song = recommend_song(get_artist('pantelis pantelidis'))
  print(song['name'], '-', song['artists'][0]['name'])

  if song['preview_url'] is not None:
    playsound(song['preview_url'])
  else:
    print('No preview: please try again')