from flask import Flask
from mongoengine import connect
# from routes.task_routes import tasks_bp
from routes.agent_ai_router import auth_bp
import certifi
import os


app = Flask(__name__)
# app.register_blueprint(tasks_bp, url_prefix="/tasks")
app.register_blueprint(auth_bp, url_prefix="/")
user_name=os.getenv("User_name")
password=os.getenv("Password")
if __name__ == "__main__":
    try:
        connect(
            db=os.getenv("DB_Name"),  # ✅ your database name (no dots)
            host=f"mongodb+srv://{user_name}:{password}@mostkbaldb.jljlksp.mongodb.net/?retryWrites=true&w=majority",
            alias="default",  # ✅ define default connection
            tlsCAFile=certifi.where(),  # ✅ SSL trust
        )

        print("✅ Connected to MongoDB Atlas successfully!")

    except Exception as e:
        print(f"✗ MongoDB connection failed: {e}")
        print(
            "💡 Tip: Make sure MongoDB Atlas credentials and IP whitelist are correct."
        )

    app.run(debug=True, port=os.getenv("Port", 8000))
