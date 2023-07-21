d1={5:"number","a":"string",(1,2):"tuple"}
print("Dictionary contents")
for x in d1.keys():
     print(x,':',d1[x],end=' ')
     print(d1[x]*3)
     print()
