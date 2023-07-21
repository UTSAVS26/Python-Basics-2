#program to find if the number is a palindrome
rev = 0
n = int(input("Enter the number: "))
#Storing the number input by user in a temp variable to run the loop
temp = n 
#Using while function to reverse the number
while temp > 0:
    digit = (temp % 10)
    rev = (rev * 10) + digit
    temp = temp // 10
#Checking if original number and reversed number are equal
if(n == rev):
    print("The entered number is a palindrome.")
else:
    print("The entered number is not a palindrome.")
