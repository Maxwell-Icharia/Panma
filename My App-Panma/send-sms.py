from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

account_sid = "AC29980fac0bf23aa64be8f1830f87cb63"
auth_token  = "3f743a7b596ee885ed8282eea0381638"

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(body="Dear, staff member your task is due and you should proceed to carry out the task.",
    to="+254710227118",
    from_="+18324632625")
except TwilioRestException as e:
    print(e)
