from flask import Blueprint,request
from controllers.ai_controller import Chat_Generalist

agentAI_bp = Blueprint("chat", __name__)

@agentAI_bp.route("/",methods=["POST"])
def Chat_ai():
    return Chat_Generalist()