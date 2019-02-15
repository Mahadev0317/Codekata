n=int(input())
a=list(map(int,input().split()))
c=1;m=1
for i in range(n-1):
  if a[i]<a[i+1]:
    c+=1
  else:
    if c>m:
      m=c
    c=1
if c>m:
  m=c
print(m)
