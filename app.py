from flask import Flask, request

app = Flask(_name_)

VERIFY_TOKEN = "ridham_ai"

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

app.run(host="0.0.0.0", port=5000)
