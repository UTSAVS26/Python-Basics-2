import random
#this list will store the questions
quiz = ["What is the capital of Uttar Pradesh?","How many states are in North-East India?\nWrite the answer in words.","Which is India\'s largest city in terms of population?","What is the national song of India?","Which Indian state has the highest literacy rate?"]
#the 'ans' list will store the correct answer
ans = ["LUCKNOW","EIGHT","MUMBAI","VANDE MATARAM","KERALA"]

#This list will store the user input
userInp = []

#This list will store the sequence of question displayed
sequence = []

#This list will be storing remarks to display as per the score
remarks =["General knowledge will always help you. Take it seriously", "Needs to take interest", "Read more to score more", "Good", "Excellent", "Outstanding"]

#This user defined function will check the score
def score():
    s = 0;
    for i in range(0,5):
        #Users answer recorded at each index is compared with the answer(using sequence to check the index)
        if(userInp[i] == ans[sequence[i]]):
            s += 1
    return s

#This function will print the remarks as per the score
def remark(score):
    print(remarks[score])

#This function will display the question as per the index passed to it
#It will also store the user input and the sequence of the question asked
def disp(r):
    print(quiz[r])
    inp = input("Answer:")
    #User input is recorded after changing it to the upper case
    userInp.append(inp.upper())
    #The sequence of the question is also recorded, to compare answers later
    sequence.append(r)                    

i = 0;
while i < 5:
    #Random number is generated between 0 to 4
    r = random.randint(0, 4)
    # If that number is not already used, it will be passed to disp function to display the question on that index
    if(r not in sequence):
        i += 1                                    
        disp(r)

#calling score function to the correct answer by each user
s = score()
print("Your score :", s, "out of 5")

#calling remark function to print the remark as per the score
remark(s)
