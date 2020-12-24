from twilio.rest import Client 
 
account_sid = 'AC208c3b8c131252fd063939cbe2da797f' 
auth_token = '70c1fcad30cc98b9869996fb4fc7ee98' 
client = Client(account_sid, auth_token) 

def sending_message(): 
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Good morning',      
                                to='whatsapp:+94756029892' 
                            ) 
 
    print(message.sid)