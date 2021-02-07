from flask import Flask, render_template
import requests
from dotenv import load_dotenv, find_dotenv
import os
import json

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
    
BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'
country = 'US'

response = requests.get(BASE_URL + "?country=" + country, headers=headers)
data = response.json()

app = Flask(__name__)

@app.route('/')
def spotify_list():
    return render_template('Spotify.html', json_data = data)


app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'))
