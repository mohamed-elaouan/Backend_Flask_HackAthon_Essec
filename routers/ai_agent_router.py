from flask import Blueprint,request
from controllers.ai_controller import 

agentAI_bp = Blueprint("auth", __name__)

@agentAI_bp.route("/",methods=["POST"])
def Chat_Bot():
    return 