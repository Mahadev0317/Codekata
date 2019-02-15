n,q=map(int,input().split())
li=list(map(int,input().split()))
lis=[]
for i in range(q):
  u,v=map(int,input().split())
  s=min(li[u-1:v])
  lis.append(s)
for i in lis:
  print(i)
