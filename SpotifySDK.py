
import requests
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

class Spotify:

    def __init__(self):
        self.URL = 'https://accounts.spotify.com/api/token'
        self.client_id = '235ae7ec8c6c416a90996380ef9e60ce'
        self.client_secret  = '6a8099f6d3aa434693e165beff43ec88'
        self.token = self.getToken()

    def getToken(self):
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=self.URL, auth=auth)

        return token['access_token']


    def refreshToken(self):
        pass
    #
    # curl - X
    # "GET" "https://api.spotify.com/v1/search?q=album%3Atest1%20artist%3Atest2&type=album&limit=1" - H
    # "Accept: application/json" - H
    # "Content-Type: application/json" - H
    # "Authorization: Bearer "




    def getSongData(self, artist, songtitle):

        q = "track:{1} artist:{0}".format(artist, songtitle)

        self.url = 'https://api.spotify.com/v1/search'
        header = {"Accept": "application/json", "Content-Type": "application/json" ,"Authorization" : "Bearer {}".format(self.token) }
        body = {'q': q,'type':'track', 'limit': '1'}
        b = requests.get(self.url, headers=header, params=body)
        return b.json()



    def addToPlaylist(self):
        pass

data = Spotify()

# a = data.getSongData('muse', 'plug in baby')

#dict_keys(['href', 'items', 'limit', 'next', 'offset', 'previous', 'total'])
#
# print(a)
# print (len(a['tracks']['items']))
# print (a['tracks']['items'][0]['uri'])
