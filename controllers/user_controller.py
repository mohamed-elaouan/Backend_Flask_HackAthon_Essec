from models.memory import UserMemory
from datetime import datetime


def get_user_memory(user_id):
    if not user_id:
        return None
    memories = UserMemory.objects(user_id=user_id).order_by("-created_at")
    return memories


def create_memory(data):
    try:
        memory = UserMemory(
            message=data.get("message"),
            response=data.get("response", "Unknown"),
            user_id=data.get("user_id"),
        )
        
        memory.save()
        return memory
    except Exception as e:
        print("Error saving memory:", e)
        return None
