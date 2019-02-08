n,m=map(int,input().split())
f=0
for i in range(n):
  a,b=map(int,input().split())
  if m in range(a,b+1):
    f=1
if f==1:
  print("yes")
else:
  print("no")
