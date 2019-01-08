n=int(input())
r=n*5
lis=[]
for i in range(0,r+1,n):
  lis.append(i)
for i in range(1,len(lis)-1):
  print(lis[i],end=" ")
print(lis[len(lis)-1])
