n=int(input())
li=list(map(int,input().split()))
s=0
lis=[]
for i in li:
  s+=i
  if s%2==0:
    lis.append(s)
  else:
    lis.append(i)
print(*lis)
