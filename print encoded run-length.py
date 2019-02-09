li=list(input())
d={}
for i in li:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
op=""
for key,value in d.items():
  op+=(key+str(value))
print(op)
#end
