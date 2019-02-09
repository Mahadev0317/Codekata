n,k=map(int,input().split())
s=bin(n*k)[2:]
c=0
for i in range(len(s)):
  if s[i]=="1":
    c+=1
print(c)
