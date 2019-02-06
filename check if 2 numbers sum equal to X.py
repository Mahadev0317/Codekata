n,m=map(int,input().split())
a=list(map(int,input().split()))
f=0
for i in range(0,n-1):
  for j in range(1,n):
    if a[i]+a[j]==m:
      print("yes")
      f=1
      break
  if f==1:
    break
else:
  print("no")
