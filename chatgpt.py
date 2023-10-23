import os

import openai
from dotenv import load_dotenv

load_dotenv()


class ChatGPT:
    def __init__(self):
        openai.api_key = os.getenv('GPT_KEY')

    def answer(self, promt):
        messages = [
            {"role": "system",
             "content": f"Ты пьяный пират, ты должен постоянно икать и вставлять шутки"},
            {"role": "user",
             "content": f"{promt}"}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages
        )
        return response['choices'][0]['message']['content']
