from flask import Flask, request, jsonify

app = Flask(_name_)

VERIFY_TOKEN = "ridham_ai"

# Home route
@app.route("/", methods=["GET"])
def home():
    return "Instagram AI Webhook Running"

# Webhook route
@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    # Meta verification request
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403

    # Handle incoming messages
    if request.method == "POST":
        data = request.get_json()
        print("Received event:", data)

        return jsonify({"status": "received"}), 200


# Run server
if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
