#Sarah
#To create a fun and interactive game that allows users to input words and generate a nonsensical story

#init
import random
#Func
print("Go crazy and Fill in these blanks down below!")
name = input("Name: ")
place = input("Place: ")
adjective = input("Adjective or random: ")
living = input("Name: ")
time = input("Pick a random number: ")
food = input("Food or random: ")
movie = input("Movie or random: ")
adjective2 = input("Adjective or random: ")

adjectivec = ["dark", "adventurous", "annoying" , "bashful" , "dry" , "fast" , "daring" , "glorious" , "fancy" , "jolly" , "mysterious" , "horrible"]

if adjective == "random":
    adjective = random.choice(adjectivec)


if adjective2 == "random":
    adjective2 = random.choice(adjectivec)


food2 = ["mc donalds", "burger king", "chinese food", "ice cream", "starbucks", "wendy's" , "portillos"]

if food == "random":
    food = random.choice(food2)


movie2 = ["it" , "Barbie", "rapunzel" , "The nun", "Five nights at freddy's", "Coraline", "Shrek"]

if movie == "random":
    movie = random.choice(movie2)


def madlibs():
    print(f"""Today I went to go hangout with my friend, \033[1m {name.upper()} \033[0m.
Their mom asked where we wanted to go and we both decided on going to \033[1m {place.upper()}\033[0m.
We had a \033[1m {adjective.upper()} \033[0m time until \033[1m {living.upper()} \033[0m came and ruined our mood.
We checked the time and saw we had spent \033[1m {time.upper()} \033[0m hours there.
It is very late and we decided to go home.
After we got home, we doordashed some \033[1m {food.upper()} \033[0m and watched the movie \033[1m {movie.upper()} \033[0m.
Today was a \033[1m {adjective2.upper()} \033[0m day and I hope to hangout with \033[1m {name.upper()} \033[0m again soon.""")


#Main
madlibs()
