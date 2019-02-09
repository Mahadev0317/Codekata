s=input()
d={}
for i in s:
  if i!=" " and i in d:
    d[i]+=1
  elif i!=" " and i not in d:
    d[i]=1
m=max(d.values())
op=""
for key,value in d.items():
  if value==m:
    op+=key
print(m,op)
