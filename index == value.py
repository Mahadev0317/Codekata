int(input())
lis=list(map(int,input().split()))
li=[]
for i in range(len(lis)):
  if lis[i]==i:
    li.append(lis[i])
if len(li)!=0:
  for i in range(len(li)-1):
    print(li[i],end=" ")
  print(li[len(li)-1])
else:
  print(-1)
