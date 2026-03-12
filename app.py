from flask import Flask, request

app = Flask(_name_)

VERIFY_TOKEN = "ridham_ai"

@app.route("/", methods=["GET"])
def home():
    return "Webhook running"

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge
    return "Verification failed"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)
    return "EVENT_RECEIVED", 200
