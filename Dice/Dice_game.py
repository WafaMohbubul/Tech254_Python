#Dice Task
#import Random Library
import random

#Welcome message to player
print("Welcome. Are you ready to play?")

#Ask user to input their name - needs to be a string
user_name = str(input("Please input your name: "))

#while loop to run through until computer or user has a bigger number
while True:
    #variables for random number generator between 1-6
    user_number = random.randint(1,6)
    computer_number = random.randint(1,6)

    #print numbers so we can see what numbers have been randomly generated
    print("User number is: ", user_number)
    print("Computer number is: ", computer_number)

    #if conditions: whoever has the bigger number is the winner.
    #if user number is bigger, then they are the winner
    if user_number > computer_number:
        print("You are the winner! Your number is greater than the Computer")
        #exit loop is user is the winner
        break
    #if the numbers are the same, then it is a tie and DO NOT EXIT LOOP. Continue in the loop
    elif user_number == computer_number:
        print("It is a tie! The number are the same")
    #Only option left is if the computer number is larger which means the computer is the winner.
    else:
        print("The computer is the winner, it has a bigger number than you!")
        #if the computer number is larger, it has won so exit the loop
        break

#Round 2 - first person to get to 30 is the winner. Ask user if they are ready for Round 2, YES or NO
user_answer = input("Are you ready for Round 2? ")

#if the user answers 'yes', then execute the while loop for the next part of the game
if user_answer.upper() == "YES":
    print("Lets get ready to Rumble!")

#while loop for the next part of the game
    while True:
        #generate 2 random numbers for user and computer from 1 to 30
        user_number_2 = random.randint(1, 30)
        computer_number_2 = random.randint(1, 30)

        #print number so audience can see what numbers are
        print("User number is: ", user_number_2)
        print("Computer number is: ", computer_number_2)

        #Loop until user OR computer reach 30.
        #if user gets 30, they are the winner
        if user_number_2 == 30:
            print("well done! You have won")
            #exit loop if they win
            break
        #if user and computer both get 30, it is a tie. Continue with loop and do not break.
        elif user_number_2 == 30 and computer_number_2 == 30:
            print("It's a tie!")
        #if computer gets 30, they are winner and exit loop.
        elif computer_number_2 == 30:
            print("The computer is the winner! Better luck next time")
            #exit loop because we have a winner
            break
#if user answers no for Round 2, do not execute while loop for game
elif user_answer.upper() == "NO":
    print("No problem. Thank you for playing!")
#if something else is answered instead of YES or NO, print invalid.
else:
    print("Invalid answer. Please select YES or NO")


