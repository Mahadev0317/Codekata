n,k=map(int,input().split())
li=list(map(int,input().split()))
f=0
for i in range(n-1):
  for j in range(i+1,n):
    if li[i]+li[j]==k:
      print("YES")
      f=1
      break
  if f==1:
    break
else:
  print("NO")
