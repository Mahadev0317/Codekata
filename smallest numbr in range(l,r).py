n,l,r=map(int,input().split())
li=list(map(int,input().split()))
lis=[]
for i in li:
  if i in range(l,r):
    lis.append(i)
print(min(lis))
