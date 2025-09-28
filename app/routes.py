from flask import Blueprint, jsonify, render_template
from app.controllers.user_ctr import register

main_bp = Blueprint("main", __name__)
@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/register", methods=["POST"])
def register_user():
    return jsonify(register())