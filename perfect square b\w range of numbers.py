n,m=map(int,input().split())
c=0
for i in range(n+1,m):
  if i**(1/2)==int(i**(1/2)):
    c+=1
print(c)
