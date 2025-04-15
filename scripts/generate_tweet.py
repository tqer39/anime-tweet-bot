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
あなたは日本のアニメに関する記念日や出来事を紹介するSNS投稿を作成するAIです。

以下の条件に従って、{date} に関連するアニメの出来事について、正確な情報に基づいた日本語のツイート文を生成してください。

条件:
- {date} に関連するアニメ『出来事（放送開始日、イベント、記念日など）を正確に記載すること。
- 情報源が不明確な場合は、日付や事実を推測せず、省略すること。
- 誤解を招く表現や曖昧な記述は避けること。
- ツイートは自然な日本語で、フォーマルすぎず、親しみやすい文体で書くこと。
- ハッシュタグや絵文字は使用しないこと。
- 出力は100文字以内とすること。

出力形式:
- ツイート本文のみを出力し、他の情報は含めないこと。
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
    content = content.replace("\n", "").replace("、", "")  # 句読点と改行を削除
    return content + "\n #アニメ #今日は何の日"


if __name__ == "__main__":
    print(generate_tweet())
