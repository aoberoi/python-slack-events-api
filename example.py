from slackeventadapter import SlackEventAdapter
from flask import Flask

slack_events = SlackEventAdapter("VERIFICATION_TOKEN")

def handle_direct_message():
    print("hi")

slack_events.on("message.im", handle_direct_message)

app = Flask(__name__)

@app.route("/")
def hello():
    print("before emit")
    slack_events.emit("message.im")
    print("after emit")
    return "Hello World!"

if __name__ == "__main__":
    app.run()
