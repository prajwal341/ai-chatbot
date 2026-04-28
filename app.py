from flask import Flask, request, jsonify, render_template
from chatbot import get_response
from database import create_db, save_chat

app = Flask(__name__)

# initialize database once
create_db()

# Home page (UI)
@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"response": "No message received"})

        user_msg = data["message"].strip()

        if user_msg == "":
            return jsonify({"response": "Empty message"})

        response = get_response(user_msg)

        # save chat to database
        save_chat(user_msg, response)

        return jsonify({"response": response})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"response": "Server error occurred"})

# Run server (IMPORTANT for Render + mobile access)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)