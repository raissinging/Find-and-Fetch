from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="", 
    from_="",
    body="Hi friend! My name is Gunner & Amora. I am a Cane Corso currently living at Poochmatch shelter in the city ofSanta Ana, CA. If you want to learn more about me and maybe take me home please visit this link: https://petsmartcharities.org/adopt-a-pet/find-a-pet/results/29213407",
    media_url= "https://pet-uploads.adoptapet.com/0/3/4/499566700.jpg") 

print(message.sid)