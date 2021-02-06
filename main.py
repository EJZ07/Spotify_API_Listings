from flask import Flask, render_template
import requests
import os

response = requests.get('https://api.spotify.com/v1/artists/{1gUi2utSbJLNPddYENJAp4}/top-tracks')
AUTH_URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = '9a99f0534e6a442581f56d58b1a97afa'

app = Flask(__name__)

@app.route('/')
def spotify_list():
    return render_template('Spotify.html')

data = response.json()

print(data)

app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP', '0.0.0.0'))
