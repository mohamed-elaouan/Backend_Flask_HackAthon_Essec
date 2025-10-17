import os
from dotenv import load_dotenv
from openai import OpenAI
from flask import request
from models.memory import UserMemory
from controllers.user_controller import get_user_memory

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
client = OpenAI(api_key=token, base_url=endpoint)
    


def Chat_without_User():
    user_data = request.cookie.get('current_user')
    if not user_data:
        response = client.chat.completions.create(
            model=model,
            # message=get__user_memory(user_id)
        )
        return {"json":response.choices[0].message.content}
    if user_data:
        response = client.chat.completions.create(
            model=model, 
            message=get_user_memory(user_data.id)
        )
        return {"json": response.choices[0].message.content}