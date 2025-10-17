from mongoengine import Document, StringField , DateTimeField
from datetime import datetime

class UserMemory(Document):
    message=StringField(required=True)
    response=StringField(required=True)
    user_id=StringField(required=False)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    