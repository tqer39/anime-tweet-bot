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
あなたは日本のアニメファン向けに「今日は何の日？」というテーマでツイートを作成するアシスタントです。

次の条件に従って、{date} に関連するアニメの出来事（放送開始、イベント、誕生日など）を日本語で140文字以内のツイートにまとめてください。

【制約条件】
- 出力は**100文字以内**としてください（140文字ではなく100文字）。
- 出力は**{date}（例：2025年4月16日）に直接関連する情報のみ**に限定してください。
- 日付と事実に**確かな出典（例：公式サイト・ニュース）**が存在しない場合は、ツイートを生成しないでください。
- 間接的・未来の予定（例：「来月放送予定」や「15年前に放送開始された」など）は使わないでください。
- 不確実な情報・主観表現・曖昧な日付（例：「○年頃」や「約○年前」）は禁止です。
- ハッシュタグ、絵文字、URLは含めないでください。
- 出力は**ツイート本文のみ**を出力し、説明や前置きは不要です。

例（良い出力）:
→ 「2012年4月16日は『這いよれ！ニャル子さん』がニコニコで配信開始された日です。」

例（悪い出力）:
× 「15年ぶりに新作が発表されました！（予定）」
× 「2025年に放送されるって話題に」
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
