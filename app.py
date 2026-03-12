from flask import Flask, request

app = Flask(_name_)

VERIFY_TOKEN = "ridham_ai"

@app.route("/")
def home():
    return "Server running"

@app.route("/webhook", methods=["GET","POST"])
def webhook():

    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403

    if request.method == "POST":
        data = request.get_json()
        print(data)
        return "EVENT_RECEIVED", 200


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
