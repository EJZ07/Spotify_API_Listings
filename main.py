from flask import Flask, render_template
import requests
from dotenv import load_dotenv, find_dotenv
import os
import json
import random

#Authorization for spotify API

AUTH_URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = '9a99f0534e6a442581f56d58b1a97afa'

load_dotenv(find_dotenv())

auth_response = requests.post(AUTH_URL, {
    
    'grant_type' : 'client_credentials',
    'client_id' : CLIENT_ID,
    'client_secret' : os.getenv('SPT_KEY'), 
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

headers = {
    'Authorization' : 'Bearer {token}'.format(token=access_token)
    }
    
SEARCH_URL = 'http://api.genius.com/search?q='
LYRICS_URL = 'http://api.genius.com/songs/'
TRACK_URL =  'https://api.spotify.com/v1/search?q='
ARTIST_URL = 'https://api.spotify.com/v1/artists?ids='
TOP_TRACKS = 'https://api.spotify.com/v1/artists/'

the_weekend = '1Xyo4u8uXC1ZmMpatF05PJ'
tobi = '4T8NIfZmVY6TJFqVzN6X49'
tyler = '4V8LLVI7PbaPR0K2TGSxFF'
healy = '2Yhge9MsE7qKcV0eWsuuHM'

market = "US"

response0 = requests.get(ARTIST_URL + the_weekend + "," + tobi + "," + tyler, headers=headers)
data0 = response0.json()

num = random.randint(0,3)
if num == 0:
    artist_info = the_weekend
elif num == 1:
    artist_info = tobi
elif num == 2:
    artist_info = tyler
elif num == 3:
    artist_info = healy
    
response1 = requests.get(TOP_TRACKS + artist_info + "/top-tracks?" + "market=" + market, headers=headers)
data1 = response1.json()

rand_track = random.randint(0, len(data1['tracks'])-1)

response_p = requests.get(TRACK_URL + data1['tracks'][rand_track]['name'] + "&type=track", headers=headers)
data_p = response_p.json()

headers = {
    'Authorization' : 'Bearer ' + os.getenv('G_ACCESS_TOKEN')
    }
response_alt = requests.get(SEARCH_URL + data1['tracks'][rand_track]['name'], headers=headers)
data_alt = response_alt.json()
response2 = requests.get(LYRICS_URL + str(data_alt['response']['hits'][0]['result']['id']), headers=headers)
data2 = response2.json()
        
app = Flask(__name__)

@app.route('/')
def spotify_list():
    return render_template('Spotify.html', preview = data_p, json_data1 = data1, g_song = data2)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'))
