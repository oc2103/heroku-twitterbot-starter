import os
import tweepy

# Load secrets
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Send tweet
try:
    api.update_status("Hello world from tweepy OAuth 1.0a!")
    print("Tweet sent successfully.")
except Exception as e:
    print("Error tweeting:", e)
