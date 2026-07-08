from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from supabase_client import supabase

app = Flask(__name__)
CORS(app)


# Load dataset.json
with open("dataset.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)


# Load knowledge.json
with open("knowledge.json", "r", encoding="utf-8") as f:
    knowledge_data = json.load(f)

knowledge = knowledge_data.get("knowledge", [])


def get_response(message):
    message = message.lower().strip()


    # 1. Search dataset.json
    for item in dataset:
        if message in item["input"].lower():
            return item["output"]


    # 2. Search Supabase
    try:
        result = (
            supabase
            .table("hanchat_ai")
            .select("*")
            .ilike("input", f"%{message}%")
            .execute()
        )

        if result.data:
            return result.data[0]["output"]

    except Exception as e:
        print("Supabase error:", e)


    # 3. Search knowledge.json (Firecrawl data)
    for item in knowledge:

        name = item.get("name", "").lower()
        category = item.get("category", "").lower()
        content = item.get("content", "")

        if (
            message in name
            or message in category
            or message in content.lower()
        ):
            return content[:1000]


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