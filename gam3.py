#game
#Random number guessing game

#init
#function
import random
import time


def easy():
    number = random.randint(0,10)
    max_attempts = 5
    attempts = 0
    score = 0
    print("I am thnking of a number between 0 and 10")
    start_time = time.time()
    while attempts < max_attempts:
        try:
            player = int( input("Enter your guess: ") )
            attempts += 1
            if player == number:
                end_time = time.time()
                time_taken = round (end_time - start_time, 2)
                if time_taken < 5:
                    score += 100
                elif time_taken < 10:
                    score += 75
                elif time_taken < 20:
                    score += 50
                else:
                    score += 25
                print("Congrats you got it right!")
                print(f"Time taken: {time_taken} seconds. Your score: {score} points.")
                break
            elif player < number:
                print("Too Low")
            else:
                print("Too High")
        except:
            print(f"Sorry, you ran out of guesses! The number was {number}.")
            print(f"Your final score: {score} points.")



def medium():
    number = random.randint(0,50)
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        try:
            player = int( input("Enter your guess: ") )
            attempts += 1
            if player == number:
                print("Congrats you got it right!")
                break
            elif player < number:
                print("Too Low")
            else:
                print("Too High")

        except ValueError:
            print("invaild input")
def hard():
    number = random.randint(0,100)
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        try:
            player = int( input("Enter your guess: ") )
            attempts += 1
            if player == number:
                print("Congrats you got it right!")
                break
            elif player < number:
                print("Too Low")
            else:
                print("Too High")

        except ValueError:
            print("invaild input")

print("Welcome! Today game is to guess the number of the day!")
mode = input("Would you like to play Easy, Medium, or Hard mode?: ")
if mode == "Easy":
    easy()
if mode == "Medium":
    medium()
else:
    hard()

