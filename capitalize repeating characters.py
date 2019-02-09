li=list(input())
r=[]
lis=[]
for i in li:
  if i in r:
    lis.append(i)
  else:
    r.append(i)
op=[]
for i in li:
  if i in lis:
    op.append(i.upper())
  else:
    op.append(i)
print("".join(op))
