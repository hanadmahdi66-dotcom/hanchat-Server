from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from supabase_client import supabase

app = Flask(__name__)

# Enable CORS for frontend connection
CORS(app)


# Load local dataset
with open("dataset.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)


def get_response(message):
    message = message.lower().strip()

    # 1. Search local JSON dataset
    for item in dataset:
        if message in item["input"].lower():
            return item["output"]

    # 2. Search Supabase database
    result = (
        supabase
        .table("hanchat_ai")
        .select("*")
        .ilike("input", f"%{message}%")
        .execute()
    )

    if result.data:
        return result.data[0]["output"]

    return "Ma fahmin 🤖"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({
            "error": "message required"
        }), 400

    message = data["message"]

    reply = get_response(message)

    return jsonify({
        "reply": reply
    })


@app.route("/")
def home():
    return jsonify({
        "status": "HanChat Backend Running 🚀"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )