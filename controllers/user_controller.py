from models.memory import UserMemory 
from controllers.user_controller import get_user_memory
from flask import jsonify

def get_user_memory(user_id):
    # if not user_id:
    if user_id:
        return UserMemory.objects(id=user_id)
    

def create_memory(data):
    try: 
        UserMemory.create
        memory = UserMemory(
                message=data.get("message"),
                response=data.get("response", "Unknown"),
                user_id=data.get("user_id"),
            )
        memory.save()
    except:
        return False



    