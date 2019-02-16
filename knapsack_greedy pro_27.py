n,W=map(int,input().split())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
p=[(v[i]/w[i]) for i in range(n)]
c=0
while W>=0 and len(p)>0:
  if W>=w[p.index(max(p))]:
    c+=v[p.index(max(p))]
    W-=w[p.index(max(p))]
  w.pop(p.index(max(p)))
  v.pop(p.index(max(p)))
  p.pop(p.index(max(p)))
print(c)
