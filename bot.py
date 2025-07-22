import os
import time
import tweepy

class TwitterAPI:
    """
    Class for accessing the Twitter API.

    Requires API credentials to be available in environment
    variables set on Render or locally.
    """
    def __init__(self):
        consumer_key = os.environ.get('CONSUMER_KEY')
        consumer_secret = os.environ.get('CONSUMER_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        """Send a tweet"""
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("Hello world!")  # You probably want to remove this line later
    while True:
        #Send a tweet here!
        time.sleep(60)
