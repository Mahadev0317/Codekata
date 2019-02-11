n,k=map(int,input().split())
s=bin(n+k)[2:]
c=0
for i in s:
  if i=="1":
    c+=1
print(c)
