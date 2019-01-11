n,k=map(int,input().split())
li=(list(map(int,input().split())))
c=0
for i in li:
  if i==k:
    c+=1
print(c)
