import os
import tweepy
import sys  # エラー終了のために sys をインポート
from generate_tweet import generate_tweet


def check_env_vars() -> None:
    """必要な環境変数が設定されているか確認"""
    required_vars = ["X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET"]
    for var in required_vars:
        if not os.getenv(var):
            print(f"Environment variable {var} is not set or empty.", file=sys.stderr)
            sys.exit(1)  # エラー終了


def post_tweet() -> None:
    # 環境変数を確認
    check_env_vars()

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

    return

    try:
        # v2 の create_tweet エンドポイントを使用してツイートを投稿
        response = client.create_tweet(text=tweet)
        print(f"Tweet posted: {response.data}")
    except tweepy.TweepyException as e:
        print(f"Failed to post tweet: {e}", file=sys.stderr)
        sys.exit(1)  # エラー終了


if __name__ == "__main__":
    post_tweet()
