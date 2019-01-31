n,k=input().split()
s=n+k
d={}
for i in s:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
print(max(d,key=d.get))
