# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+1mynumber", #no spaces or parens
    from_="+1twilionumber", #no spaces or parens
    body="You have light inside you. And when you let it out, you can change the world around you.")