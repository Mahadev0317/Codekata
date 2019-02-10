n=int(input())
li=list(map(int,input().split()))
d={}
for i in li:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
m=min(d.values())
for k,v in d.items():
  if v==m:
    print(k)
