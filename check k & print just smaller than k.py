n,k=map(int,input().split())
li=list(map(int,input().split()))
f=0
for i in range((k-min(li))+1):
  for j in li:
    if j==k:
      print(k)
      f=1
      break   
  else:
    k-=1
    f=0
  if f==1:
    break
