from twilio.rest import Client
from credential import my_sid, my_auth_token, my_cell, my_twilio

client=Client(my_sid,my_auth_token)
my_msg="hello buddy!!"##enter your message
message=client.messages.create(to=my_cell,from_=my_twilio,body=my_msg)
##then simply run file(send.py) and wait for the message in your mobile
