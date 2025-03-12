from django.conf import settings
from twilio.rest import Client
import os

def send_sos_sms(phone, latitude, longitude,user):
    """Sends an SOS alert with location using Twilio SMS API."""
    TWILIO_ACCOUNT_SID= None
    TWILIO_AUTH_TOKEN= None
    TWILIO_PHONE_NUMBER= None

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    # Google Maps link with live location
    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    
    message_body = f"🚨 SOS ALERT! 🚨\nEmergency for {user.first_name} !Please help!\nLive Location: {maps_link}"

    try:
        message = client.messages.create(
            body=message_body,
            
            from_=TWILIO_PHONE_NUMBER,
            to=str("+91"+phone)
        )
        return f"Message sent successfully! SID: {message.sid}"
    
    except Exception as e:
        return f"Failed to send SMS: {str(e)}"
    
