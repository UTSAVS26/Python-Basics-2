# Python code to find occurrence of any element 
# appearing 'n' times
# Input Initialisation
input = [1, 2, 3, 0, 4, 3, 4, 0, 0]
# Sort Input
input.sort()
# Constants Declaration
n = 3
prev = -1
count = 0
flag = 0
# Iterating
for item in input:
     if item == prev:
          count = count + 1
     else:
          count = 1
     prev = item
     if count == n:
          flag = 1
          print("There are {} occurrences of {} in {}".
                format(n, item, input))
          break
# If no element is not found.
if flag == 0:
     print("No occurrences found")
