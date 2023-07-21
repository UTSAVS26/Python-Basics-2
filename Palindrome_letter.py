s=input("Please enter a string: ")
s2=[x for x in s]
s2.reverse()
if s=="".join(s2):
     print("The string is a palindrome")
else:
     print("The string is not a palindrome")
