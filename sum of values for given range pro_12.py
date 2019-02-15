n,q=map(int,input().split())
li=list(map(int,input().split()))
lis=[]
for i in range(q):
  u,v=map(int,input().split())
  s=0
  for i in range(u-1,v):
    s+=li[i]
  lis.append(s)
for i in lis:
  print(i)
