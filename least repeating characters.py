l=list(input())
d={}
for i in l:
  if i!=" ":
    if i in d:
      d[i]+=1
    else:
      d[i]=1
lis=[]
for key,value in d.items():
  if value==1:
    lis.append(key)
print(*lis)
