n,q=map(int,input().split())
li=[]
for i in range(n+1,q):
  if i%2==0:
    li.append(i)
for i in range(0,len(li)-1):
  print(li[i],end=" ")
print(li[len(li)-1])
