#100 birds of the World
#The purpose of my program is to ask user what color birds they are interested in and their diet and will give the output of if the bird is endangered or not and the name of it.


#Initialize
import pandas as pd #Used to read the CSV file
import webbrowser #Used to open images of birds
import time #Used for pausing
data = pd.read_csv('birds.csv') #Load data from CSV file


id = data['id'].tolist() #Number of bird
name = data['Name'].tolist() #Name of bird
scientific = data['Scientific Name'].tolist() #The scientific name of the bird
status = data['Conservation Status'].tolist() #Knowing if the bird is endangered, Near Threaten, or Least Concern
color = data['Primary Color'].tolist() #The colors of birds in this array
diet = data['Diet'].tolist() #The diets of the bird
imager = data['Image of Range'].tolist()
image = ["https://www.allaboutbirds.org/guide/assets/photo/63737371-480px.jpg",
    "https://www.allaboutbirds.org/guide/assets/og/75229331-1200px.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/cd/Setophaga_ruticilla_-Chiquimula%2C_Guatemala_-male-8-4c.jpg",
    "https://static.wikia.nocookie.net/animals/images/2/2c/IMG_6372.jpg/revision/latest/scale-to-width-down/340?cb=20140808205058",
    "https://media.nationalgeographic.org/assets/photos/000/277/27700.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/1/1a/About_to_Launch_%2826075320352%29.jpg",
    "https://tilandtrust.org/sites/default/files/images/news/belted_kingfisher_s52-13-028_l.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/191086401/320",
    "https://i.pinimg.com/736x/b3/71/e7/b371e7cec9f6762ae1d81a3e43cc3daf.jpg",
    "https://www.allaboutbirds.org/guide/assets/photo/59859171-480px.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Chiroxiphia_caudata-2.jpg",
    "https://farm9.staticflickr.com/8806/17074254082_97daffe794_z.jpg",
    "https://i.pinimg.com/originals/bf/06/c9/bf06c92782159121e579866191c6c08e.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/203317581/1800",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/219318871/1800",
    "https://www.allaboutbirds.org/guide/assets/og/75302131-1200px.jpg",
    "https://www.allaboutbirds.org/guide/assets/photo/68122191-480px.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/143000061/900",
    "https://cdn.mos.cms.futurecdn.net/z3iEY8ryHdNzeyvLxyMppT.jpg",
    "https://www.allaboutbirds.org/guide/assets/og/75368221-1200px.jpg",
    "https://www.allaboutbirds.org/guide/assets/photo/300152741-480px.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/45128851/1800",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/70583361/1800",
    "https://www.allaboutbirds.org/guide/assets/og/75340411-1200px.jpg",
    "https://photofeathers.files.wordpress.com/2011/03/img_5056.jpg",
    "https://www.ontarioparks.com/parksblog/wp-content/uploads/2015/10/canstockphoto2749376.jpg",
    "https://www.birdguides-cdn.com/cdn/gallery/birdguides/e4d0baee-75dc-424e-a76f-ecbfda56c1da.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/275821031/1800",
    "https://www.allaboutbirds.org/guide/assets/og/75351601-1200px.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Emperor_goose_by_Lisa_Hupp_USFWS.jpg/220px-Emperor_goose_by_Lisa_Hupp_USFWS.jpg",
    "https://www.birdsofcolombia.org/world/Flame_Bowerbird_Male.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/44495661/1800",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/296730461/1800",
    "https://i2.wp.com/www.beyourownbirder.com/wp-content/uploads/2018/05/golden-white-eye.jpg?fit=670%2C300",
    "https://www.birdsville.net.au/wp-content/uploads/2011/07/Gouldian-finch1.jpg",
    "https://avibirds.com/wp-content/uploads/2020/08/great-blue-heron-400x442.jpg",
    "https://i.pinimg.com/originals/62/8b/a5/628ba5fefe540ae3bc80c4b2a81b3a81.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/191038011/320",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Great_hornbill_Photograph_by_Shantanu_Kuveskar.jpg/330px-Great_hornbill_Photograph_by_Shantanu_Kuveskar.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/244162041/1200",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/140480041/1800",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flamant_rose_Salines_de_Thyna.jpg/1200px-Flamant_rose_Salines_de_Thyna.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Harpia_harpyja_001_800.jpg/330px-Harpia_harpyja_001_800.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/1/1a/Black-necked_Stilt.jpg",
    "https://wildlatitudes.com/wp-content/uploads/Hoatzin_by_Murray-Foubister.jpg",
    "https://www.pbs.org/wnet/nature/files/2014/08/1200468kpo10-1024x682.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIvgz4jXeQSVtLJGvrgs-8lwaTVKUXFO-kbw&usqp=CAU",
    "https://olivemacawparrotsfarm.com/wp-content/uploads/2019/11/Laughing-Falcon-Herpetotheres-cachinnans.jpg",
    "https://animals.sandiegozoo.org/sites/default/files/2016-11/animals_hero_kookaburra.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/188555631/1800",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1CTaVtQcXuxJV6tI0N9ZTbdML_Xep99yWAg&usqp=CAU",
    "https://www.animalspot.net/wp-content/uploads/2014/07/Macaroni-Penguin-Images.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/b/bf/Anas_platyrhynchos_male_female_quadrat.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/b/b7/Mourning_Dove_2006.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/158687851/1800",
    "https://abcbirds.org/wp-content/uploads/2016/06/Nene_Jack-Jeffrey_PR.jpg",
    "https://www.biorxiv.org/content/biorxiv/early/2020/05/14/2020.05.12.092080/F1.large.jpg",
    "https://i.ytimg.com/vi/gj_q3rpHF6g/maxresdefault.jpg",
    "https://www.allaboutbirds.org/guide/assets/photo/160654851-480px.jpg",
    "https://images.fineartamerica.com/images-medium-large-5/pied-avocet-recurvirostra-avosetta-panoramic-images.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Pileated_Woodpecker_%289597212081%29%2C_crop.jpg/220px-Pileated_Woodpecker_%289597212081%29%2C_crop.jpg",
    "https://innerstrength.zone/wp-content/uploads/2020/02/3_result_result2.jpg",
    "https://www.allaboutbirds.org/guide/assets/photo/94974451-480px.jpg",
    "https://alchetron.com/cdn/razorbill-0c5144ab-deca-47c2-b7f1-ec251841176-resize-750.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Buphagus_erythrorhynchus00.jpg/330px-Buphagus_erythrorhynchus00.jpg",
    "https://nas-national-prod.s3.amazonaws.com/styles/article_teaser/s3/editorial-card-images/article/ed-card_apa_2013_28356_226452_megumiaita_redbreasted_nuthatch_kk.jpg?itok=0jjmRsgs",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/171755111/1800",
    "https://i.pinimg.com/originals/1e/14/1e/1e141e9b56b19a76b72dab5db07d2716.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/173557351/1800",
    "https://www.allaboutbirds.org/guide/assets/photo/71316071-480px.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Paloma_brav%C3%ADa_%28Columba_livia%29%2C_Palacio_de_Nymphenburg%2C_M%C3%BAnich%2C_Alemania01.JPG/330px-Paloma_brav%C3%ADa_%28Columba_livia%29%2C_Palacio_de_Nymphenburg%2C_M%C3%BAnich%2C_Alemania01.JPG",
    "https://nas-national-prod.s3.amazonaws.com/styles/hero_cover_bird_page/s3/a1_5380_8_roseate-spoonbill_andrew_mccullough_adult.jpg?itok=sulRVtJC",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/193674311/320",
    "https://cdn.birdwatchingdaily.com/2013/06/Kinglet-Ruby-crowned-10-0089-660x440.jpg",
    "https://i.pinimg.com/originals/7d/23/79/7d2379ac656c56ec5e31c67672b2ceb0.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/221182651/1800",
    "https://www.allaboutbirds.org/guide/assets/photo/67449631-480px.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/220892221/1800",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Accipiter_striatus%2C_Canet_Road%2C_San_Luis_Obispo_1.jpg/330px-Accipiter_striatus%2C_Canet_Road%2C_San_Luis_Obispo_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/c0/Balaeniceps_rex.jpg",
    "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/243730471/1800",
    "https://galapagosconservation.org.uk/wp-content/uploads/2018/12/Smooth-billed-Ani-Crotophaga-ani-Divine-Farm-29-1-2010-2-small-1000x667.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/2/28/Schneckenweih-Snail-Kite.JPG",
    "https://www.treehugger.com/thmb/rYPDZsLevHn5WBs-XuwMdi6BLuk=/4192x3144/smart/filters:no_upscale()/__opt__aboutcom__coeus__resources__content_migration__mnn__images__2020__01__snowy_owl_flying-cdff0730fab6435d8d0e1edffda3ca21.jpg",
    "https://i.ytimg.com/vi/H26Tl7e3KeU/maxresdefault.jpg",
    "https://www.allaboutbirds.org/news/wp-content/uploads/2018/06/14-Vogelkop_sing_Tim_Laman_ML_Feature-1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/68/Tawny_Frogmouth_-_Sydney_Olympic_Park.jpg",
    "https://www.animalspot.net/wp-content/uploads/2016/02/Toco-Toucans.jpg",
    "https://www.allaboutbirds.org/guide/assets/og/81386391-1200px.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/e5/Tufted_Puffin_Alaska_%28cropped%29.jpg",
    "https://img.theepochtimes.com/assets/uploads/2020/05/18/Victoria-Crowned-Pigeon-i.jpg",
    "https://i.pinimg.com/736x/dd/42/54/dd425491e9c313330e407d4c7894edb6.jpg",
    "https://www.purelypoultry.com/images/vulturine-guineafowl_04.jpg",
    "https://www.shanghaibirding.com/wp-content/uploads/2020/02/white-wagtail-ocularis.jpg",
    "https://cdn.birdwatchingdaily.com/2019/09/Whooping-Crane-Aransas-NWR_8109-Welty.jpg",
    "https://i.ytimg.com/vi/BvIuUABZkiI/maxresdefault.jpg",
    "https://bloximages.newyork1.vip.townnews.com/yakimaherald.com/content/tncms/assets/v3/editorial/3/03/303e8cea-73fa-11e6-841c-cfeef8ca8b2d/57ce60c1369f6.image.jpg?crop=1662%2C935%2C0%2C155&resize=1662%2C935&order=crop%2Cresize",
    "https://www.allaboutbirds.org/guide/assets/photo/65051941-480px.jpg"] #Images of the birds


birds = [] #To add the name of birds into this array
birds2 = [] #To add information of the user input
birds3 = [] #Another one to add more information to display to the user


#Function


#Function is used to ask users for which color bird they are interested in learning more about
def birdcolor(user_color): #Function is asking user to pick a color between the ones listed
    found = False
    for i in range(len(color)): #When user input is found in the color array
        if user_color in color[i]:
            webbrowser.open(image[i]) #Displays image
            birds.append({name[i]}) #Tells the name of bird(s)
            birds2.append({scientific[i]}) #The scientific name
            birds3.append({status[i]}) #To know if they are safe or endangered
            found = True
    if not found: #If user either can mispell or chooses a color that is not in the color list
        print("Unable to find color of bird. Please try again or pick a different option!") #It tells user how it is not in the list and takes them back to the options list
        return
    print(f"""The birds that are this colored are:
        {birds} """)
    time.sleep(1.25) #To give a little time for the user to read the information
    print("꩜")
    time.sleep(1.25)
    print("꩜ ꩜")
    time.sleep(1.25)
    print("꩜ ꩜ ꩜")
    time.sleep(1.25)
    print(f"""The birds scienfiic name are:
        {birds2}.""")
    time.sleep(1.25)
    print("꩜")
    time.sleep(1.25)
    print("꩜ ꩜")
    time.sleep(1.25)
    print("꩜ ꩜ ꩜")
    time.sleep(1.25)
    print(f"""The bird(s) Conservation Status is:
        {birds3}.""")
    birds.clear()
    birds2.clear()
    birds3.clear()




#Function is used to ask user a type of food a bird(s) can possibliy eat
def diet1(user_diet):
     found = False
     for i in range(len(diet)):
          if user_diet in diet[i]:
               webbrowser.open(image[i])
               birds.append(name[i])
               birds2.append(diet[i])
               birds3.append(status[i])
               found = True
     if not found:
         print("This food is not found in diet. Please try again or pick another option!")
         return
     print(f"""The bird(s) that have this diet are:
           {birds}""")
     time.sleep(1.25)
     print("꩜")
     time.sleep(1.25)
     print("꩜ ꩜")
     time.sleep(1.25)
     print("꩜ ꩜ ꩜")
     time.sleep(1.25)
     print(f"""The bird(s) full diet is:
           {birds2}""")
     time.sleep(1.25)
     print("꩜")
     time.sleep(1.25)
     print("꩜ ꩜")
     time.sleep(1.25)
     print("꩜ ꩜ ꩜")
     time.sleep(1.25)
     print(f"""The bird(s) conservation status:
           {birds3}""")
     birds.clear()
     birds2.clear()
     birds3.clear()




#Function is used to show users whether or not a bird is endangered
def stat(user_stat):
     found = False
     for i in range(len(status)):
          if user_stat in status[i]:
               webbrowser.open(image[i])
               birds.append(name[i])
               birds2.append(scientific[i])
               found = True
     if not found:
         print("Invaild input. Please try again or pick a different option to look at!")
         return
     print(f"""The bird(s) name are:
           {birds}""")
     time.sleep(1.25)
     print("꩜")
     time.sleep(1.25)
     print("꩜ ꩜")
     time.sleep(1.25)
     print("꩜ ꩜ ꩜")
     time.sleep(1.25)
     print(f"""The bird(s) scientific name are:
           {birds2}""")
     birds.clear()
     birds2.clear()
     birds3.clear()






def Menu():
    input("""^^^Today we will be looking at 100 birds around the world.^^^
    You learn more about which birds are endangered/Nearly threaten/Least Concern.
    Press Enter to contiune. """)
    while True:
        ask = input("""--- Would you like to ---


    A. Look at images of birds based on their color, learn their scientific name, and conservation status?
    B. Look at images of birds based on their diet?
    C. Look at birds that are threaten and how they look like?
    D. Quit.


    Type letter here: """). capitalize()
        if ask == 'A':
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            user = input("""There are many types of colored birds around the world!
    Looking at these 100 birds, they are the colors: yellow, blue, black, white, grey, brown, green, red, pink.
    Which colored bird(s) are you interested to learn more about? """).capitalize()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            birdcolor(user)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


        elif ask == 'B':
             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
             user2 = input("""Many birds diet depends on the shape of their Beak
    A birds diet can contain:
    Seeds, insects, leaves, fruit, etc
    But some birds like an eagle can eat frogs, fish, small mammals, small lizards, etc
    Type a food in: """).lower()
             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
             diet1(user2)
             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


        elif ask == 'C':
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            user3 = input("""Would you like to know which birds are:
              Least = Concern
              Near = Threatened
              Endangered
              Type here: """).capitalize()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            stat(user3)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


        elif ask == 'D':
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("I hope you enjoyed learning about birds! Goodbye!")
            break
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Invaild input please try again.")


#Main
Menu()


#Dataset Source Information:
#100 birds dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://www.birds.cornell.edu/home/


#Source Information:
#Website Name: birds.cornell.edu
#Url: https://www.birds.cornell.edu/
#Organization group name(author): CornellLab
#Article Name: CornellLab
#Date: January 15, 2015


#Symbols
#Copy and Paste symbols
#Website Name: coolsymbols.top
#Url: https://www.coolsymbol.top/
#Symbol ꩜ source: https://www.coolsymbol.top/
