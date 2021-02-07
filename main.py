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
    
TRACK_URL = 'https://api.spotify.com/v1/tracks/'
ARTIST_URL = 'https://api.spotify.com/v1/artists?ids='
TOP_TRACKS = 'https://api.spotify.com/v1/artists/'

the_weekend = '1Xyo4u8uXC1ZmMpatF05PJ'
birocratic = '60b7IDlGflg5lgyfEGf9yB'
tyler = '4V8LLVI7PbaPR0K2TGSxFF'

market = "US"

response = requests.get(TRACK_URL + '62PclpoBFLl50PJpiJA5RT', headers=headers)
data = response.json()

response0 = requests.get(ARTIST_URL + the_weekend + "," + birocratic + "," + tyler, headers=headers)
data0 = response0.json()

num = random.randint(0,2)
if num == 0:
    artist_info = the_weekend
elif num == 1:
    artist_info = birocratic
elif num == 2:
    artist_info = tyler
    
response1 = requests.get(TOP_TRACKS + artist_info + "/top-tracks?" + "market=" + market, headers=headers)
data1 = response1.json()
        
app = Flask(__name__)

@app.route('/')
def spotify_list():
    return render_template('Spotify.html', json_data = data, json_data0 = data0, json_data1 = data1)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'))
