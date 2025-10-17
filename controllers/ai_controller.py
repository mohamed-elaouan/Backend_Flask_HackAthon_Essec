import os
from dotenv import load_dotenv
from openai import OpenAI
from flask import request, jsonify
from models.memory import UserMemory
from controllers.user_controller import get_user_memory, create_memory
import json

load_dotenv()

# 🔹 Load API token and endpoint (GitHub Models or OpenAI)
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"  # GitHub Models endpoint

# ✅ Use correct initialization — only once
client = OpenAI(api_key=token, base_url=endpoint)

# 🔹 Model name
model = "gpt-4o-mini"  # or "gpt-4.1-mini"

def Chat_Generalist():
    try:
        # 1️⃣ Get JSON body
        body = request.get_json(silent=True) or {}
        message = body.get("message")
        user_id = body.get("user_id")

        if not message:
            return jsonify({"error": "Message not provided"}), 400

        # 2️⃣ Prepare messages
        messages = [{"role": "user", "content": message}]

        # 3️⃣ Retrieve and include previous memory
        if user_id:
            previous_memory = get_user_memory(user_id)
            if previous_memory:
                for mem in previous_memory:
                    # Assuming mem.message and mem.response exist
                    messages.insert(0, {"role": "assistant", "content": mem.response})
                    messages.insert(0, {"role": "user", "content": mem.message})

        # 4️⃣ Get response from model
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        response_text = response.choices[0].message.content

        # 5️⃣ Save memory
        create_memory(
            data={
                "message": message,
                "response": response_text,
                "user_id": user_id or "guest",
            }
        )

        # 6️⃣ Return final response
        return jsonify({"response": response_text})

    except Exception as e:
        print("❌ Error in Chat_Generalist:", e)
        return jsonify({"error": str(e)}), 500
