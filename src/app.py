import os
from twilio.rest import Client
import json

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']


def lambda_handler(event, context):
    body = json.loads(event['body'])
    to_phone_number = body.get('phone_number')
    district = body.get('district')
    send_sms(to_phone_number, district)


def send_sms(to_phone_number, district):
    if not to_phone_number:
        raise ValueError("Missing 'to_phone_number' parameter")

    client = Client(account_sid, auth_token)
    # takes in phone number and district to send the text message with the correct link
    message = client.messages.create(
        to=to_phone_number, 
        from_=twilio_phone_number,
        body=f"Don't forget to complete your forms for your SportsPhysicals+. Use this link ASAP! https://patient.pond.md/{district}/welcome")

    print(message.sid)

