import os
import tweepy
from generate_tweet import generate_tweet


def post_tweet():
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuth1UserHandler(
        api_key, api_secret, access_token, access_token_secret
    )
    api = tweepy.API(auth)

    tweet = generate_tweet()
    api.update_status(tweet)


if __name__ == "__main__":
    post_tweet()
