n=int(input())
li=list(map(int,input().split()))
lis=[]
s=sum(li)
if n==1:
  print(*li)
else:
  for i in range(len(li)):
    s+=li[i]
    lis.append(s)
    s=sum(li)
  print(*lis)
