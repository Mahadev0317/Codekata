n,q=map(int,input().split())
li=list(map(int,input().split()))
def gcd(x,y):
  while(y):
    x,y=y,x%y
  return x
lis=[]
for i in range(q):
  l,r=map(int,input().split())
  if l==r:
    lis.append(l)
  else:
    g=gcd(li[l-1],li[l])
    for j in range(l+1,r):
      g=gcd(g,li[j])
    lis.append(g)
for i in lis:
  print(i)
