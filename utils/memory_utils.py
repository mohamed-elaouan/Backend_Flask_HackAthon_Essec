from models.memory import UserMemory


def get__user_memory(user_id):
    # if not user_id:
    if user_id:
        return UserMemory.objects(id=user_id)
    