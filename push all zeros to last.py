n=int(input())
li=list(map(int,input().split()))
c=0
lis=[]
for i in li:
  if i==0:
    c+=1
  else:
    lis.append(i)
for i in range(c):
  lis.append(0)
print(*lis)
