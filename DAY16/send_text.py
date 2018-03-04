# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC9739aa99a8f2022cff74ca53275349c9"
auth_token = "f118a6a4d9f3890557ba2e1cb755a1c7"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+386434397",
    body="SMS-Text Message from Gjergj Kadriu",
    from_="+38618280365",
)

print(message.sid)
