#Program to Convert a String into Title Case.
def convertToTitle(string):
    titleString = string.title();
    print("The input string in title case is:",titleString)
userInput = input("Write a sentence: ")
totalSpace = 0
for b in userInput:
    if b.isspace():
        totalSpace += 1
if(userInput.istitle()):
    print("The String is already in title case")
elif(totalSpace > 0):
    convertToTitle(userInput)
else:
    print("The String is of one word only")
