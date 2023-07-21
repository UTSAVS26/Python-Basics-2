# n = 3 Number of lines from top to middle of diamond shape
n = 3
for i in range (1, n + 1):
          # This will print the space  
    space = (n - i)*" "
          # It will print the star
    star =  (2 * i - 1)*"*"
    print(space,star)
# The bottom half will be drawn using this loop
for j in range(n - 1, 0, -1):
    space = (n - j)*" "
    star = (2 * j - 1)*"*"
    print(space, star)
