import random

#defining options to take input from the user
def options():
    print("\n\nWhat would you like to practice today?")
    print("1. Addition")
    print("2. Two(2) letters words")
    print("3. Three(3) letter words")
    print("4. Word Substitution")
    print("5. Exit")
    inp=int(input("Enter your choice(1-5)"))
    
    #calling the functions as per the input
    if inp == 1:
        sumOfDigit()
    elif inp == 2:
        twoLetterWords()
    elif inp == 3:
        threeLetterWords()
    elif inp == 4:
        wordSubstitution()
    elif inp == 5:
        return
    else:
        print("Invalid Input. Please try again\n")
        options()

#Defining a function to provide single digit addition with random numbers
def sumOfDigit():
    x = random.randint(1,9)
    y = random.randint(1,9)
    print("What will be the sum of",x,"and",y,"? ")
    z = int(input())
    if(z == (x+y)):
        print("Congratulation...Correct Answer...\n")
        a = input("Do you want to try again(Y/N)? ")
        if a == "n" or a == "N":
            options()
        else:
            sumOfDigit()
    else:
        print("Oops!!! Wrong Answer...\n")
        a = input("Do you want to try again(Y/N)? ")
        if a == "n" or a == "N":
            options()
        else:
            sumOfDigit()        

#This function will display the two letter words
def twoLetterWords():
    words = ["up","if","is","my","no"]
    i = 0
    while i < len(words):
        print("\n\nNew Word: ",words[i])
        i += 1
        inp = input("\n\nContinue(Y/N):")
        if(inp == "n" or inp == "N"):
            break;
    options()

#This function will display the three letter words
def threeLetterWords():
    words = ["bad","cup","hat","cub","rat"]
    i = 0
    while i < len(words):
        print("\n\nNew Word: ",words[i])
        i += 1
        inp = input("Continue(Y/N):")
        if(inp == "n" or inp == "N"):
            break;
    options()

#This function will display the word with missing character
def wordSubstitution():
    words = ["b_d","c_p","_at","c_b","_at"]
    ans = ["a","u","h","u","r"]
    i = 0
    while i < len(words):
        print("\n\nWhat is the missing letter: ",words[i])
        x = input()
        if(x == ans[i]):
            print("Congratulation...Correct Answer...\n")
        else:
            print("Oops!!!Wrong Answer...\n")
        i += 1
        inp = input("Continue(Y/N):")
        if(inp == "n" or inp == "N"):
            break;
    options()

#This function call will print the options and start the program
options()
