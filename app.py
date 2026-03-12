from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "ridham_ai"

@app.route("/webhook", methods=["GET","POST"])
def webhook():
    
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == VERIFY_TOKEN:
            return challenge
        return "Verification token mismatch", 403

    if request.method == "POST":
        data = request.json
        print(data)
        return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
