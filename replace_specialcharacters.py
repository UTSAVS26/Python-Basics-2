# Function to Replace special characters in the string with a specified character
def remover(my_string):
     for item in my_string:
          if item not in values:
               my_string = my_string.replace(item, "")
     return my_string
values = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
str12=input("Enter a String: ")
print(remover(str12))
