# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
# tutorial at https://www.twilio.com/docs/quickstart/python/sms
# and ngrok tutorial at https://www.twilio.com/blog/2013/10/test-your-webhooks-locally-with-ngrok.html
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

app.secret_key = "hostesswiththemostest"


@app.route("/")
def index():
    """Homepage"""
    return "Hello, World!"


@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
