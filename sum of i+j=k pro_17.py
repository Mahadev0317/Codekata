n,k=map(int,input().split())
a=list(map(int,input().split()))
f=0
for i in range(n-1):
  for j in range(i+1,n):
    if a[i]+a[j]==k:
      print("yes")
      f=1
      break
  if f==1:
    break
else:
  print("no")
