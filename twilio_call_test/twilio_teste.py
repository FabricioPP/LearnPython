from twilio.rest import Client #Chama a classe cliente do modulo twilio.rest


# SID da sua conta, encontre em twilio.com/console
account_sid = "AC7efb7150287d452fc8725df8d1daac07"
# Seu Auth Token, encontre em twilio.com/console
auth_token  = "8ccd6cc5cd06ed324d58acdfd6b918b3"

client = Client(account_sid, auth_token) #Instancia a classe cliente e chama o construtor passando dois parametros



call = client.calls.create(
    to="+5535984434914", 
    from_="+554139075373",
    url="https://handler.twilio.com/twiml/EH93cee988cf07f6624e09d2813dc88898"
    )

print(call.sid)