n,k=map(int,input().split())
s=bin(n+k)[2:]
c=0
if n==k:
  print(0)
else:
  for i in s:
    if i=="1":
      c+=1
  print(c)
