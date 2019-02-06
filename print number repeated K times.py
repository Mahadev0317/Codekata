n,k=map(int,input().split())
l=list(map(int,input().split()))
d={}
for i in l:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
for key,value in d.items():
  if value==k:
    print(key)
