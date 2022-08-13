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



#print(petSmartURL(zip="91711", age= "senior", breedID= "real=800", color = "152", distance="250", size = "", sex = "m"))
# zip is just the zip

age = ["young", "adult", "senior", "puppy"]

color_dict = { "Black": "152" , "Brindle": "153", "Brown" : "154", "Chocolate": "154",
"Gray": "155", "Blue" : "155", "Silver": "155", "Salt & Pepper" : "155", "Merle": "156",
"Red" : "157", "Golden": "157", "Orange": "157", "Chestnut" : "157", "Silver & Tan" : "158",
"Tan" : "159", "Yellow" : "159", "Fawn" : "159", "Tricolor" : "160", "White" : "161" }

distance = ["35", "50", "75", "100", "250"]

size_dict = {"small" : 1, "med" : 2, "large" : 3, "xl" : 4}

sex_dict = {"male": "m", "female": "f"}




breeds =  {'Gentle Giants': 'criteria=1081',
 'Mutt-Madness Surprise Mix!': 'criteria=1063',
 'Mini Mutts (Mucho Love!)': 'criteria=1073',
 'Mid-Sized Mutts': 'criteria=1064',
 'Big Mutt-hatten Sky Scrapers': 'criteria=1077',
 'Barrymore\'s Buddies': 'super=1017',
 'Taco Bell Dog\'s Little Amigos': 'nick=1033',
 'Eddie & Frasier\'s Friends!': 'nick=1048',
 'Affenpinscher': 'real=187',
 'Afghan Hound': 'real=1',
 'Ain\'t Nothin\' but a Hound Dog!': 'super=1015',
 'Airedale Terrier': 'real=2',
 'Akbash': 'real=800',
 'Akita': 'real=3',
 'Alaskan Malamute': 'real=4',
 'Almost a Horse': 'criteria=1078',
 'American Bulldog': 'real=361',
 'American Eskimo Dog': 'real=5',
 'American Hairless Terrier': 'real=1167',
 'American Pit Bull Terrier': 'real=801',
 'American Staffordshire Terrier': 'real=1082',
 'American Water Spaniel': 'nick=1030',
 'Anatolian Shepherd': 'real=7',
 'Australian Cattle Dog': 'real=8',
 'Australian Kelpie': 'real=9',
 'Australian Shepherd': 'real=10',
 'Australian Terrier': 'real=802',
 'Basenji': 'real=12',
 'Basset Griffon Vendeen': 'nick=1053',
 'Basset Hound': 'real=13',
 'Beagle': 'real=14',
 'Bearded Collie': 'real=15',
 'Beauceron': 'real=803',
 'Bedlington Terrier': 'real=189',
 'Belgian Laekenois': 'real=1168',
 'Belgian Malinois': 'real=191',
 'Belgian Shepherd': 'real=16',
 'Belgian Tervuren': 'real=192',
 'Bernese Mountain Dog': 'real=17',
 'Bichon Frise': 'real=18',
 'Black Mouth Cur': 'real=804',
 'Black and Tan Coonhound': 'real=19',
 'Bloodhound': 'real=20',
 'Blue Heeler': 'nick=1027',
 'Blue Lacy/Texas Lacy': 'real=1368',
 'Bluetick Coonhound': 'real=193',
 'Bobtail': 'nick=1041',
 'Bolognese': 'real=1165',
 'Border Collie': 'real=21',
 'Border Terrier': 'real=194',
 'Borzoi': 'real=22',
 'Boston Terrier': 'real=23',
 'Bouvier des Flandres': 'real=24',
 'Boxer': 'real=25',
 'Boykin Spaniel': 'real=601',
 'Briard': 'real=26',
 'Brittany': 'real=27',
 'Brussels Griffon': 'real=195',
 'Bull Terrier': 'real=28',
 'Bulldog': 'nick=1039',
 'Bullmastiff': 'real=30',
 'Cairn Terrier': 'real=31',
 'Canaan Dog': 'real=381',
 'Canary Dog': 'nick=1194',
 'Cane Corso': 'real=461',
 'Cardigan Welsh Corgi': 'nick=1036',
 'Carolina Dog': 'real=805',
 'Carry-On Size Cuties': 'criteria=1074',
 'Catahoula Leopard Dog': 'real=33',
 'Cattle Dog': 'nick=1028',
 'Cavalier King Charles Spaniel': 'real=34',
 'Chesapeake Bay Retriever': 'real=35',
 'Chihuahua': 'real=36',
 'Chinese Crested': 'real=37',
 'Chinook': 'real=1374',
 'Chow Chow': 'real=38',
 'Clumber Spaniel': 'real=196',
 'Cockapoo': 'real=39',
 'Cocker Spaniel': 'real=40',
 'Collie': 'real=41',
 'Coonhound': 'real=42',
 'Coonhounds (All Types)': 'super=1014',
 'Corgi': 'real=230',
 'Coton de Tulear': 'real=521',
 'Curly-Coated Retriever': 'real=1169',
 'Cute Canine Crosses': 'criteria=1070',
 'Dachshund': 'real=44',
 'Dalmatian': 'real=45',
 'Dandie Dinmont Terrier': 'real=199',
 'Deerhound': 'nick=1060',
 'Doberman Pinscher': 'real=46',
 'Dogo Argentino': 'real=621',
 'Dogue de Bordeaux': 'real=242',
 'Dutch Shepherd': 'real=47',
 'English (Redtick) Coonhound': 'real=1186',
 'English Bulldog': 'real=29',
 'English Mastiff': 'nick=1052',
 'English Pointer': 'nick=1173',
 'English Setter': 'real=49',
 'English Sheepdog': 'nick=1042',
 'English Shepherd': 'real=641',
 'English Springer Spaniel': 'real=51',
 'English Toy Spaniel': 'real=52',
 'Entlebucher': 'real=808',
 'Eskimo Dog': 'nick=1020',
 'Eskimo Spitz': 'nick=1019',
 'Fantastic Fidos': 'criteria=1067',
 'Feist': 'real=310',
 'Field Spaniel': 'real=201',
 'Fila Brasileiro': 'real=810',
 'Finnish Lapphund': 'real=811',
 'Finnish Spitz': 'real=54',
 'Flat-Coated Retriever': 'real=202',
 'Fox Terrier (Smooth)': 'real=812',
 'Fox Terrier (Toy)': 'real=813',
 'Fox Terrier (Wirehaired)': 'real=55',
 'Fox Terriers (All Types)': 'super=1005',
 'Foxhound': 'real=56',
 'French Bulldog': 'real=203',
 'French Mastiff': 'nick=1038',
 'Funny-Faced Breeds': 'super=992',
 'German Pinscher': 'real=814',
 'German Shepherd Dog': 'real=57',
 'German Shorthaired Pointer': 'real=58',
 'German Wirehaired Pointer': 'real=204',
 'Giant Schnauzer': 'nick=1171',
 'Glen of Imaal Terrier': 'real=815',
 'Go Fetch! Retrievers!': 'super=1016',
 'Golden Retriever': 'real=60',
 'Goldendoodle': 'real=1369',
 'Gordon Setter': 'real=61',
 'Great Dane': 'real=62',
 'Great Pyrenees': 'real=63',
 'Greater Swiss Mountain Dog': 'real=205',
 'Greyhound': 'real=64',
 'Halden Hound (Haldenstrover)': 'real=661',
 'Harrier': 'real=206',
 'Havanese': 'real=501',
 'Hounds (All Types)': 'super=1006',
 'Hounds (Scent Hounds)': 'super=1008',
 'Hounds (Sight Hounds)': 'super=1007',
 'Hovawart': 'real=816',
 'Hungarian Puli': 'nick=1195',
 'Hungarian Water Dog': 'nick=1196',
 'Husky': 'real=817',
 'Ibizan Hound': 'real=281',
 'Irish Setter': 'real=67',
 'Irish Terrier': 'real=207',
 'Irish Water Spaniel': 'real=208',
 'Irish Wolfhound': 'real=68',
 'Italian Greyhound': 'real=69',
 'Italian Spinone': 'real=818',
 'Jack Russell Terrier': 'real=70',
 'Japanese Chin': 'real=71',
 'Jindo': 'real=72',
 'Just Right (Not too big or small)': 'criteria=1066',
 'Kai Dog': 'real=819',
 'Karelian Bear Dog': 'real=820',
 'Keeshond': 'real=73',
 'Kerry Blue Terrier': 'real=209',
 'King Charles Spaniel': 'nick=1032',
 'Kishu': 'real=821',
 'Komondor': 'real=210',
 'Kuvasz': 'real=74',
 'Kyi Leo': 'real=822',
 'Labradoodle': 'real=1170',
 'Labrador Retriever': 'real=823',
 'Lakeland Terrier': 'real=211',
 'Lancashire Heeler': 'real=826',
 '"Lassie\'s Friends!"': 'nick=1034',
 'Leonberger': 'real=827',
 'Lhasa Apso': 'real=76',
 'Little Fluffy Powder-Puffs of Love': 'super=991',
 'Little Lovers': 'criteria=1076',
 'Löwchen': 'real=1187',
 'Maltese': 'real=77',
 'Manchester Terrier': 'real=78',
 'Maremma Sheepdog': 'real=828',
 'Marvelous Mixes': 'criteria=1065',
 'Mastiff': 'real=200',
 'Mastiffs (All Types)': 'super=1001',
 'Mexican Hairless': 'nick=1061',
 'Miniature Pinscher': 'real=80',
 'Miniature Poodle': 'nick=1054',
 'Miniature Schnauzer': 'nick=1058',
 'Mountain Cur': 'real=829',
 'Munsterlander': 'real=830',
 'Muscle-Bound Momma\'s Boys (& Girls!)': 'nick=1026',
 'Muttchkins': 'criteria=1075',
 'Mutts are Great, Don\'t Discriminate!': 'criteria=1072',
 'Neapolitan Mastiff': 'real=83',
 'Newfoundland': 'real=84',
 'Norfolk Terrier': 'real=214',
 'Norwegian Buhund': 'real=831',
 'Norwegian Elkhound': 'real=85',
 'Norwich Terrier': 'real=215',
 'Nova Scotia Duck-Tolling Retriever': 'real=832',
 'Old English Sheepdog': 'real=302',
 'Otterhound': 'real=87',
 'Papillon': 'real=88',
 'Parson Russell Terrier': 'nick=1172',
 'Patterdale Terrier (Fell Terrier)': 'real=833',
 'Pekingese': 'real=89',
 'Pembroke Welsh Corgi': 'nick=1035',
 'Petit Basset Griffon Vendeen': 'real=216',
 'Pharaoh Hound': 'real=90',
 'Pit Bull Terrier': 'nick=1021',
 'Plott Hound': 'real=581',
 'Podengo Portugueso': 'real=834',
 'Pointer': 'real=92',
 'Polish Lowland Sheepdog': 'real=1166',
 'Pomeranian': 'real=93',
 'Poochy Pals': 'criteria=1069',
 'Poodle (Miniature)': 'real=213',
 'Poodle (Standard)': 'real=94',
 'Poodle (Toy or Tea Cup)': 'real=226',
 'Poodles (All Types)': 'super=1010',
 'Portuguese Water Dog': 'real=95',
 'Presa Canario': 'real=1188',
 'Pug': 'real=96',
 'Puli': 'real=1189',
 'Pumi': 'real=835',
 'Pup-pourri': 'criteria=1068',
 'Rat Terrier': 'real=218',
 'Redbone Coonhound': 'real=664',
 'Redtick Coonhound': 'nick=1193',
 'Retrievers (All Types)': 'super=1011',
 'Rhodesian Ridgeback': 'real=98',
 'Rottweiler': 'real=99',
 'Russian Wolfhound': 'nick=1029',
 'Saluki': 'real=101',
 'Samoyed': 'real=102',
 'Schiller Hound': 'real=662',
 'Schipperke': 'real=103',
 'Schnauzer (Giant)': 'real=836',
 'Schnauzer (Miniature)': 'real=837',
 'Schnauzer (Standard)': 'real=104',
 'Schnauzers (All Types)': 'super=1013',
 'Scottie, Scottish Terrier': 'real=105',
 'Scottish Deerhound': 'real=219',
 'Sealyham Terrier': 'real=220',
 'Setters (All Types)': 'super=1012',
 'Shar Pei': 'real=107',
 'Sheep & Herding Dogs': 'super=994',
 'Sheltie, Shetland Sheepdog': 'real=108',
 'Shepherds (All Types)': 'super=1002',
 'Shiba Inu': 'real=110',
 'Shih Tzu': 'real=111',
 'Siberian Husky': 'nick=1084',
 'Silky Terrier': 'real=113',
 'Skye Terrier': 'real=221',
 'Sloughi': 'real=841',
 'Smooth Fox Terrier': 'nick=1044',
 'Snow Dogs (Husky/Fluffy Types)': 'super=993',
 'Spaniels (All Types)': 'super=998',
 'Spaniels (Medium)': 'super=1000',
 'Spaniels (Small)': 'super=999',
 'Spitz Types (Large)': 'super=995',
 'Spitz Types (Medium)': 'super=996',
 'Spitz Types (Small)': 'super=997',
 'Springer Spaniel': 'nick=1043',
 'St. Bernard': 'real=100',
 'Staffordshire Bull Terrier': 'nick=1022',
 'Standard Poodle': 'nick=1055',
 'Standard Schnauzer': 'nick=1059',
 'Strong but Sweet': 'nick=1024',
 'Super-Sized Sweeties': 'criteria=1080',
 'Sussex Spaniel': 'real=222',
 'Swedish Vallhund': 'real=846',
 'Tea Cup Poodle': 'nick=1057',
 'Terriers (Medium)': 'super=1004',
 'Terriers (Small)': 'super=1003',
 'Thai Ridgeback': 'real=561',
 'Tibetan Mastiff': 'real=224',
 'Tibetan Spaniel': 'real=225',
 'Tibetan Terrier': 'real=118',
 'Tons of Love': 'criteria=1079',
 'Tosa Inu': 'real=848',
 'Toto\'s Little pals from Oz!': 'nick=1031',
 'Tough & Tender': 'nick=1025',
 'Toy Fox Terrier': 'nick=1046',
 'Toy Poodle': 'nick=1056',
 'Treeing Walker Coonhound': 'real=119',
 'Vizsla': 'real=120',
 'Weimaraner': 'real=121',
 'Welsh Corgi': 'nick=1037',
 'Welsh Springer Spaniel': 'real=849',
 'Welsh Terrier': 'real=227',
 'Westie, West Highland White Terrier': 'real=123',
 'Wheaten Terrier': 'real=124',
 'Whippet': 'real=125',
 'Wirehaired Fox Terrier': 'nick=1045',
 'Wirehaired Pointing Griffon': 'real=127',
 'Xoloitzcuintle/Mexican Hairless': 'real=212',
 'Yorkie, Yorkshire Terrier': 'real=244',
 '31 Flavors Mixes': 'criteria=1071' }