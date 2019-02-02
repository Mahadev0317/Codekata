n,m,k=input().split()
n=sorted(n);m=sorted(m)
k=int(k)
c=0
for i in range(max(len(n),len(m))):
  if n[i]!=m[i]:
    c+=1
if c==k:
  print("yes")
else:
  print("no")
