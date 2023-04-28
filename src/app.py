import os
from twilio.rest import Client
import json
import re

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']


def handler(event, context):
    body = json.loads(event['body'])
    to_phone_number = body.get('phone_number')
    district = body.get('district')
    send_sms(to_phone_number, district)


def send_sms(to_phone_number, district):
    if not to_phone_number:
        raise ValueError("Missing 'to_phone_number' parameter")
    
        # Remove all non-numeric characters from the phone number
    phone_number = re.sub(r'\D', '', to_phone_number)
    
    # Check if the phone number already includes the country code
    if phone_number.startswith('1'):
        formatted_phone_number = '+' + phone_number
    elif len(phone_number) == 10:
        formatted_phone_number = '+1' + phone_number
    else:
        # Return an error message if the phone number is not valid
        return {'error': 'Invalid phone number'}

    client = Client(account_sid, auth_token)
    # takes in phone number and district to send the text message with the correct link
    message = client.messages.create(
        to=formatted_phone_number, 
        from_=twilio_phone_number,
        body=f"Don't forget to complete your forms for your SportsPhysicals+. Use this link ASAP! https://patient.pond.md/{district}/welcome")
    print(message.sid)

