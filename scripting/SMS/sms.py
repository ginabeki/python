#twillio
from twilio.rest import Client 
 
account_sid = 'ACbb9238293c32a2851cb1b628666aab69' 
auth_token = 'auth_token' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='xx',                          body='message',      
                              to='+254' 
                          ) 
 
print(message.sid)