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
    """Dynamically respond to incoming messages depending on the country of origin."""

    # determine the country where the text is coming from
    from_country = request.values.get('FromCountry', None)

    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Hi! It looks like you're calling from " + from_country)

    return str(resp)

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
