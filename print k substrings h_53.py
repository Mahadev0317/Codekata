li,k=input().split()
li=list(li);k=int(k)
op=[]
for i in range(0,len(li)):
  if len(li[i:i+k])==k:
    op.append("".join(li[i:i+k]))
print(*op)
