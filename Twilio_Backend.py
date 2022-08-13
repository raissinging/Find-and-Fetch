from twilio.rest import Client
import time
import schedule
from Webscraping import run_all_pages, dog_info

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

def main(zip="", age="", breedID="", color="", distance="", size="", 
            sex="", species = "dog"): 
    return None


old_dog_list=run_all_pages(zip, age, breedID, color, distance, size, sex, species)
while True: 
    new_dog_list=run_all_pages(zip, age, breedID, color, distance, size, sex, species)
    old=old_dog_list.set()
    new=new_dog_list.set()
    overlap=new.difference(old)
    if len(overlap) !=0: 
        for elem in overlap: 
            message,image=dog_info(elem)



    #execute function 
    schedule.run_pending()
    time.sleep(3600)