from twilio.rest import Client

# Sends a text message using Twilio's API.
# media_url requires a list of HTTP addresses to send images.
account_sid = ""
auth_token = ""

def send_sms(to="", text="", urls=[]):
	Client(account_sid, auth_token).messages.create(
		to = to,
		from_ = "",
		body = text,
		media_url = urls)
