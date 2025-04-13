import os
import tweepy
from generate_tweet import generate_tweet


def post_tweet() -> None:
    bearer_token = os.getenv("X_BEARER_TOKEN")  # v2エンドポイント用のBearer Token
    if not bearer_token:
        raise ValueError("X_BEARER_TOKEN is not set in environment variables.")

    client = tweepy.Client(bearer_token=bearer_token)  # Bearer Token のみを使用

    tweet = generate_tweet()
    try:
        response = client.create_tweet(text=tweet)  # v2エンドポイントでツイートを投稿
        print(f"Tweet posted: {response.data}")
    except tweepy.TweepyException as e:
        print(f"Failed to post tweet: {e}")


if __name__ == "__main__":
    post_tweet()
