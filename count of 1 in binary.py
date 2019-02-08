n=int(input())
s=bin(n)[2:]
c=0
for i in s:
  if int(i)==1:
    c+=1
print(c)
