n = 5
for i in range (1, n + 1):
    #This will print the space before the number
    space = (n - i) * "  "
    print(space, end = " ")
    #This for loop will print the decreasing numbers
    for k in range(i, 1, -1):
        print(k, end = " ")
    #This for loop will print the increasing numbers
    for j in range(1, i + 1):
        print(j, end = " ")
    #Print a new line after the space and numbers are printed
    print()
