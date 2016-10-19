from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

account_sid = "AC29980fac0bf23aa64be8f1830f87cb63" # Your Account SID from www.twilio.com/console
auth_token  = "3f743a7b596ee885ed8282eea0381638"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)



try:
    message = client.messages.create(body="Hey Ivy",
    # to="+254710227118",    # Replace with your phone number
    to="+254701511738",    # Replace with your phone number
    from_="+18324632625") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
