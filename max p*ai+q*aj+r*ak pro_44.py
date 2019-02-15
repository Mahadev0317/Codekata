n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(n):
  for j in range(i,n):
    for k in range(j,n):
      if p*a[i]+q*a[j]+r*a[k]>c:
        c=p*a[i]+q*a[j]+r*a[k]
print(c)
