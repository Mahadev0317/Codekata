s,k=input().split()
op=[]
for i in range(int(k)-1,len(s),int(k)):
  op.append(s[i])
print(*op)
