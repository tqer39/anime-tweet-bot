from openai import OpenAI
import os
from datetime import datetime

# Set OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key is not set.")

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_tweet() -> str:
    model = os.getenv("OPENAI_MODEL", "gpt-4")  # 新しいモデルを指定
    date = datetime.now().strftime("%Y年%m月%d日")
    prompt = f"""
今日は{date}です。

アニメや声優に関連する「今日は何の日？」の雑学を最大3件、140文字以内で紹介してください。
日本のX（旧Twitter）向けに、句読点や改行を適度に入れつつ、一般人が「へえ」と思えるような内容にしてください。

最後に適度なハッシュタグ（#今日は何の日、#アニメ、#声優 など）を付けてください。
"""
    response = client.chat.completions.create(
        model=model,  # 新しい ChatCompletion API を使用
        messages=[
            {"role": "system", "content": "あなたは日本のアニメや声優に詳しいアシスタントです。"},
            {"role": "user", "content": prompt},
        ],
        max_tokens=200,
        temperature=0.7,
    )
    content = response["choices"][0]["message"]["content"]
    if not isinstance(content, str):
        raise TypeError("Expected a string in the response content")
    return content.strip()


if __name__ == "__main__":
    print(generate_tweet())
