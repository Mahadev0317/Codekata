n,k=map(int,input().split())
s=bin(n*k)[2:]
op=[]
for i in range(len(s)):
  if s[i]=="1":
    op.append(i+1)
print(op[1])
