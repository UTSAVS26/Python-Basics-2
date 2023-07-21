#Program to Replace a Whitespace with Hyphen.
def replaceChar(string):
    return string.replace(' ','-')
userInput = input("Enter a sentence: ")
result = replaceChar(userInput)
print("The new sentence is:",result)
