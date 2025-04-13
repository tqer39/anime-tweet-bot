import os
import tweepy
from generate_tweet import generate_tweet


def post_tweet() -> None:
    # Twitter API v2 クライアントを作成
    client = tweepy.Client(
        consumer_key=os.getenv("X_API_KEY"),
        consumer_secret=os.getenv("X_API_SECRET"),
        access_token=os.getenv("X_ACCESS_TOKEN"),
        access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET"),
    )

    print("Generating tweet...")
    tweet = generate_tweet()
    print(f"Tweet generated: {tweet}")

    try:
        # v2 の create_tweet エンドポイントを使用してツイートを投稿
        response = client.create_tweet(text=tweet)
        print(f"Tweet posted: {response.data}")
    except tweepy.TweepyException as e:
        print(f"Failed to post tweet: {e}")


if __name__ == "__main__":
    post_tweet()
