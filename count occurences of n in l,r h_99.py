l,r,n=map(int,input().split())
op=0
def occur(x):
  c=0;i=0
  while i<len(x):
    if i+len(str(n))>len(str(x)):
      break
    elif x[i:i+len(str(n))] == str(n):
      c+=1
      i=i+len(str(n))
    else:
      i+=1
  return c
for i in range(l,r):
  op+=occur(str(i))
print(op)
