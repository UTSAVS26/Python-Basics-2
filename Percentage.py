# Program of print a grade
n=int(input("Enter the marks of Student: "))
if n>=90:
     print("You get A grade.")
elif (n>=75 and n<=90):
     print("You get B grade.")
elif (n>=60 and n<=75):
     print("You get D grade.")
elif (n<60):
     print("You get E grade.")
else:
     print("""Please Enter Valid Number
           Program terminated!!!!!""")
