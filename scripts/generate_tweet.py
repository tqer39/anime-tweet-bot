import openai
import os
from datetime import datetime


def generate_tweet():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "text-davinci-003")  # デフォルトモデルを指定
    date = datetime.now().strftime("%Y年%m月%d日")
    prompt = f"""
今日は{date}です。

アニメや声優に関連する「今日は何の日？」の雑学を最大3件、140文字以内で紹介してください。
日本のX（旧Twitter）向けに、句読点や改行を適度に入れつつ、一般人が「へえ」と思えるような内容にしてください。

最後に適度なハッシュタグ（#今日は何の日、#アニメ、#声優 など）を付けてください。
"""
    response = openai.Completion.create(
        engine=model,  # モデルを指定
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    print(generate_tweet())
