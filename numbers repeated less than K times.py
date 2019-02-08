n,m=map(int,input().split())
li=list(map(int,input().split()))
d={}
lis=[]
for i in li:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
for k,v in d.items():
  if v<m:
    lis.append(k)
print(*lis)
