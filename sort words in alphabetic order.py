li=list(input().split())
lis=[]
for i in li:
  lis.append(sorted(list(i)))
op=[]
for i in lis:
  op.append("".join(i))
print(*op)
