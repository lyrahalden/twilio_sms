# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
import os
import datetime


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12092104311", #no spaces or parens
    from_="+14247850086", #no spaces or parens
    body="Greetings! The current time is: " + str(datetime.datetime.now()) + " ECATL8U6TATK39N")