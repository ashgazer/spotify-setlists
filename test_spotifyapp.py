from SpotifySDK import Spotify

def test_callSpotify():
    assert Spotify()


def test_callGetToken():

    obj = Spotify

    obj.getToken()