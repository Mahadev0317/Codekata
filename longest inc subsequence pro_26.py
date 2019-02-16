n=int(input())
a=list(map(int,input().split()))
c=1;i=0
while i<n-1:
  j=i+1
  if a[j]>a[i]:
    c+=1
    break
  i+=1
for i in range(j,n-1):
  if a[i]<a[i+1]:
    c+=1
print(c)
