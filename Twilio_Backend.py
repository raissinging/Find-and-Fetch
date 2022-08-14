from twilio.rest import Client
import time
import schedule
from Webscraping import run_all_pages, dog_info

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

TEXT_ENABLE=False

def main(toNum, old_dog_list, fromNum = "#", zipcode="", age="", breedID="", color="", distance="", size="", 
            sex="", species = "dog"): 

    #old_dog_list=run_all_pages(zipcode, age, breedID, color, distance, size, sex, species)

    if TEXT_ENABLE == True: 
        message=client.messages.create(
                        to=toNum, 
                        from_=fromNum,
                        body='Hello from Find and Fetch. Thank you for taking the first step to adopting your furry friend. We will send you a message if we find a new potential fit based on your criteria. Reply "STOP" to stop receiving updates.')
        while True: 
            new_dog_list=run_all_pages(zipcode, age, breedID, color, distance, size, sex, species)
            old=old_dog_list.set()
            new=new_dog_list.set()
            overlap=new.difference(old)
            if len(overlap) !=0: 
                for elem in overlap: 
                    messagebody,image=dog_info(elem)
                    message = client.messages.create(
                        to=toNum, 
                        from_=fromNum,
                        body=messagebody,
                        media_url= image) 
                    print(message.sid)
                    
            schedule.run_pending()
            time.sleep(86400)


# main()



