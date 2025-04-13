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
    model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    date = datetime.now().strftime("%Y年%m月%d日")
    prompt = f"""
今日は{date}です。

- アニメや声優に関連する「今日は何の日？」の雑学を最大3件紹介してください。
- 日本のX（旧Twitter）向けに、句読点や改行を適度に入れつつ、一般人が「へえ」と思えるような内容にしてください。
- ハッシュタグは含めない。
- 文字列タグなどすべて含めて絶対に100文字以内厳守。オーバーすると投稿エラーになるため。
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
    return str(response.choices[0].message.content).strip() + "\n #アニメ #今日は何の日"


if __name__ == "__main__":
    print(generate_tweet())
