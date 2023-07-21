# Program to check whether a string is palindrome or not.
str14=input("Enter a String: ")
l=len(str14)
p=l-1
index=0
while (index<p):
     if (str14[index]==str14[p]):
          index+=1
          p-=1
     else:
          print("String is not a Palindrome")
          break
else:
     print("String is a Palindrome")
