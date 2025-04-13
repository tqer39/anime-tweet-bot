import os
import tweepy
from generate_tweet import generate_tweet


def post_tweet() -> None:
    bearer_token = os.getenv("X_BEARER_TOKEN")  # v2エンドポイント用のBearer Token
    client = tweepy.Client(bearer_token=bearer_token)

    tweet = generate_tweet()
    response = client.create_tweet(text=tweet)  # v2エンドポイントでツイートを投稿
    print(f"Tweet posted: {response.data}")


if __name__ == "__main__":
    post_tweet()
