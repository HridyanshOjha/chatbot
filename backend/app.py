
import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
print("API KEY:", api_key)
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return "Backend with Gemini API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = model.generate_content(user_message)
        bot_reply = response.text
    except Exception as e:
        bot_reply = "Error generating response. Please try again."

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)