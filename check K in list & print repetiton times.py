n,k=map(int,input().split())
li=list(map(int,input().split()))
d={}
for i in li:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
for key,value in d.items():
  if key==k:
    print("yes",value)
    break
else:
  print("no")
