#Nickname
#Student will ask questions to the user in order to find out which celebrity the user is

#Function
def celebrity():

    #Collect Data
    print("Hello! Want to know which celebrity you are? Just answer the following questions!")
    social = input("Are you a social person (extroverted or intorverted)? ")
    #Extroverted person
    if social == "extroverted":
        party = input("Do you to like A) Party or B) Hangout with your friends (A or B)? ")
        if party == "A":
            make = input("Do you like to A) make the parties or B) Go to them (A or B)? ")
            if make == "A":
                print("You are like the celebrity: Kim Kardashian")
            else:
                print("You are like the celebrity: Paris Hilton")
        else:
            ms = input("Do you like to hangout at A) Resturants or B) Go to stores or movies (A or B)? ")
            if ms == "A":
                print("You are like the celebrity: Selena Gomez")
            else:
                print("You are like the celebrity: Lana Del Rey")

    #Introverted person
    if social == "introverted":
        Activity = input("Do you like to A) Watch movies or B) Draw (A or B)? ")
        if Activity == "A":
            movie = input("Do you like to A) Watch scary movies or B) Watch romantic movies (A or B)? ")
            if movie == "A":
                print("You are like the celebrity: Lady Gaga")
            else:
                print("You are like the celebrity: Ryan Gosling")
        else:
            watch = input("Do you like to draw A) Anime or B) Cartoons (A or B)? ")
            if watch == "A":
                print("You are like the celebrity: Billie Eilish")
            else:
                print("You are like the celebrity: Megan Thee Stallion")

#Main
celebrity()
