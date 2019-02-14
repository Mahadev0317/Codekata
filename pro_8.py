n,q=map(int,input().split())
li=list(map(int,input().split()))
lis=[]
for i in range(q):
  l,r=map(int,input().split())
  if l==r:
    lis.append(li[l-1])
  else:
    lis.append(1)
for i in lis:
  print(i)
