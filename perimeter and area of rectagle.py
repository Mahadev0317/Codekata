n,a=map(int,input().split())
p=(n//2)-1
for i in range(1,p+1):
  if i*p==a:
    print("yes")
    break
  else:
    p-=1
else:
  print("no")
