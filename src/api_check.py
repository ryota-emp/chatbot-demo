import os

import openai
from dotenv import load_dotenv

'''
FROM https://platform.openai.com/docs/quickstart
'''
# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAI APIキーを設定
openai.api_key = os.getenv('OPENAI_API_KEY')

# Chat
completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # 有効なモデル名を使用
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "自己紹介をした上で、あなたにどのようなことができるかを説明して"
        }
    ]
)

# 応答内容を取得して表示
response_content = completion.choices[0].message.content
print(response_content)