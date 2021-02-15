# Project 1 -Spotify API

This demo explains how to call the spotify API using the Python request library and parsing it with JSON data.
It also shows how you can stire and hide your API keys with a `.env` file and `.gitignore` file, respectively.

##Requirements
1. `pip install ptyhon-dotenv`
2. `pip install Flask`
3. `pip install requests`

##Setup
1. Go to https://developer.spotify.com/documentation/web-api/quick-start/ to set up a developers account
2. Retrieve the Client ID and Secret key from https://developer.spotify.com/dashboard/applications
3. Use the authorization url, https://accounts.spotify.com/api/token to post a request
4. Create `.env` file in your main directory
5. Add Secret key with the line: `export SPT_KEY = 'YOUR_KEY'`, and another line `export G_ACCESS_TOKEN = 'YOUR_KEY'`

##Run Application
1. Run command in terminal `python main.py`
2. See output of favorite artists and songs 

##Deploy Heroku
1. Install Heroku CLI: `npm install -g heroku`
2. Create a Heroku account on https://signup.heroku.com/login
3. Create a `requirements.txt` that contains `Flask`, `requests`, `python-dotenv`
4. Create a Procfile which contains the line `web: python main.py` 
5. Add + commit all changed files with git
6. Login in to Heroku: `heroku login -i`
7. Create a Heroku app: `heroku create`
8. Push your code to Heroku: `git push heroku main`
9. Add the secret keys from the `.env` with the matching variable (`SPT_KEY`) and (`G_ACCESS_TOKEN`) and their respective values
10. Run `heroku open` 

##Questions
a. Three technical issues I've encountered with my project: 
    1. Gaining authorization to access the Spotify API was an issue as connection to Spotify's API is a different process
    2. The external style sheet would not update when changed.Changing the name from `styles.css` to something else fixed the issue
    3. Many Urls I constructed to reach the Spotify API would not extract the data, because of certain syntactiacal errors
c. I hope to improve on Html and CSS beautification. There's text and images in places I don't want them to be, and the page overall looks very uninteresting.