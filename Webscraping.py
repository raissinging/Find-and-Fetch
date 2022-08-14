import requests
from bs4 import BeautifulSoup

def petSmartURL(zip="", age="", breedID="", color="", distance="", size="", 
sex="", species = "dog", page_num = 1):

    """
    """
    url = "https://petsmartcharities.org/adopt-a-pet/find-a-pet?ab=US_adoptions_find-a-store-adoption-kit_&"

    age_url = "age=" + age
    breed_url = "&breed_id=" + breedID
    zip_url = "&city_or_zip=" + zip
    color_url = "&color_id=" + color
    distance_url = "&geo_range=" + distance 
    size_url = "&miniSubmit=yes&pet_size_range_id=" + size
    sex_url = "&sex=" + sex
    species_url = "&species=" + species
    page_num_url = "&page_number=" + str(page_num)

    url += age_url + breed_url + zip_url + color_url + distance_url + size_url + sex_url + species_url + page_num_url
    
    return url

def getDogs(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.findAll('div',attrs={'class':'aap-pet-photo'})
    dogs = []
    for div in data:
        links = div.findAll('a')
        for a in links:
            dogs.append(a['href'])

    return dogs 

def run_all_pages(zip="", age="", breedID="", color="", distance="", size="", 
                 sex="", species = "dog"):
    dog_list = []
    page_num = 1
    url = petSmartURL(zip, age, breedID, color, distance, size, sex, species, page_num) 
    dog_list_temp = getDogs(url)
    dog_list.extend(dog_list_temp)

    while dog_list_temp != []:
        page_num+=1
        url = petSmartURL(zip, age, breedID, color, distance, size, sex, species, page_num) 
        dog_list_temp = getDogs(url)
        dog_list.extend(dog_list_temp)

    return dog_list

    
def dog_info(dog):
    page = requests.get(dog)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find('div',attrs={'class':'pet-detail-page__info__pet__detail'}).h1.getText()
    breed = soup.find('div',attrs={'class':'pet-detail-page__info__pet__detail'}).h4.getText()
    shelter = soup.find('p',attrs={'class':'pet-location-details shelter'}).getText()
    city = soup.find('p',attrs={'class':'pet-location-details city'}).getText()
    image = soup.find('div',attrs={'class':'pet-detail-page__images__full col-12 col-md-9'}).img["src"]
    ret = "Hi friend! My name is " + name + ". I am a " + breed + ' currently living at the shelter, "' + shelter + '", in the city of ' + city + ". If you want to learn more about me and maybe take me home please visit this link: " + dog
    return (ret, image)


url = "https://petsmartcharities.org/adopt-a-pet/find-a-pet?ab=US_adoptions_find-a-store-adoption-kit_030215&age=young&breed_id=criteria=1081&city_or_zip=91750&color_id=155&geo_range=50&miniSubmit=yes&pet_size_range_id=1&sex=m&species=dog"
#url = "https://petsmartcharities.org/adopt-a-pet/find-a-pet?city_or_zip=91750&species=dog&cats_or_dogs=dog&other_pets=_none&age=adult&breed_id=nick%3D1037&color_id=153&geo_range=50&pet_size_range_id=1&sex=m&form_build_id=form-QlvScU8QKP6YVhrycwgRIeQSKRtS5GuL28apZZzFfVE&form_id=adopt_a_pet_search_form"
dogs = getDogs(url)

dog_info(dogs[2])









