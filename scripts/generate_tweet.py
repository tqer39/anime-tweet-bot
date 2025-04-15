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

- アニメや声優に関連する「今日は何の日？」の雑学を1件紹介してください。
- 公式情報や wikipedia に掲載されている情報を元にしてください。
- ハルシネーションを避けてください。
- 日本のX（旧Twitter）向けに、一般人が「へえ」と思えるような内容にしてください。
- 句読点や改行、ハッシュタグは含めない。
- 絵文字は少し使って。
- 文字列タグなどすべて含めて絶対に100文字以内厳守。オーバーすると投稿エラーになるため。
"""
    response = client.chat.completions.create(
        model=model,
        web_search_options={
            "search_context_size": "medium",
            "user_location": {
                "type": "approximate",
                "approximate": {
                    "country": "JP",
                },
            },
        },
        messages=[{"role": "user", "content": prompt}],
    )
    content = str(response.choices[0].message.content).strip()
    lines = content.split("\n")  # 行ごとに分割
    while sum(len(line) for line in lines) > 100:  # 合計文字数が100を超える場合
        lines.pop()  # 最後の行を削除
    return "\n".join(lines) + "\n #アニメ #今日は何の日"


if __name__ == "__main__":
    print(generate_tweet())
