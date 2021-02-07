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
5. Add Secret key with the line: `export SPT_KEY = 'YOUR_KEY'`

##Run Application
1. Run command in terminal `python main.py`
2. See output of favorite artists and songs 

##Questions
a. Three technical issues I've encountered with my project: 
    1. Gaining authorization to access the Spotify API was an issue as connection to Spotify's API is a different process
    2. The external style sheet would not update when changed.Changing the name from `styles.css` to something else fixed the issue
    3. Many Urls I constructed to reach the Spotify API would not extract the data, because of certain syntactiacal errors
c. I hope to improve on Html and CSS beautification. There's text and images in places I don't want them to be, and the page overall looks very uninteresting.