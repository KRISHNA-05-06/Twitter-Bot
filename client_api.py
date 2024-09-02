import tweepy

def clientapi(bearer_token,api_key,api_secret,access_token,access_token_secret):
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
    return client