list1=[2,3,3,2,5,3,2,5,1,1]
counts={}
ct=0
lst=[]
for num in list1:
     if num not in lst:
          lst.append(num)
          counts[num]=0
     ct=ct+1
     counts[num]=counts[num]+1
print(counts)
for key in counts.keys():
     counts[key]=key*counts[key]
print(counts)
