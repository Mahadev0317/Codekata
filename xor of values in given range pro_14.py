n,q=map(int,input().split())
li=list(map(int,input().split()))
lis=[]
for i in range(q):
  u,v=map(int,input().split())
  xor=li[u-1]
  for i in range(u,v):
    xor=xor^li[i]
  lis.append(xor)
for i in lis:
  print(i)
