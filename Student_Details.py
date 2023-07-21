SCL=dict()
i=1
flag=0
n=int(input("Enter number of entries: "))
while i<=n:
     Adm=input("\nEnter admission number of a student: ")
     nm=input("Enter name of a student: ")
     section=input("Enter class and section: ")
     per=float(input("Enter percentage of a student: "))
     b=(nm,section,per)
     SCL[Adm]=b
     i+=1
l=SCL.keys()

for i in l:
     print("\nAdmno- ",i,"   :")
     z=SCL[i]
     print("Name\t","Class\t","Percentage\t")
     for j in z:
          print(j,end="\t")
