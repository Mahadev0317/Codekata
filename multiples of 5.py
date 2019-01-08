n=int(input())
s=0
lis=[]
for i in range(0,5):
  s+=n
  lis.append(s)
for i in range(0,len(lis)-1):
  print(lis[i],end=" ")
print(lis[len(lis)-1])
