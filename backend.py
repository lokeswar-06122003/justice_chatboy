from flask import Flask, request, jsonify
from database import save_chat
import openai

app = Flask(__name__)

# OpenAI API Key
openai.api_key = "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"


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    prompt = f"Provide legal information based on the following query: {user_input}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    bot_response = response["choices"][0]["message"]["content"]
    save_chat(user_input, bot_response)  # Save to MongoDB

    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(debug=True)

