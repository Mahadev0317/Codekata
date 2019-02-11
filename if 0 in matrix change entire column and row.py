n,k=map(int,input().split())
m=[]
for i in range(n):
  li=list(map(int,input().split()))
  m.append(li)
i1=[];j1=[]
for i in range(n):
  for j in range(k):
    if m[i][j]==0:
      i1.append(i)
      j1.append(j)
for i in i1:
  for j in range(k):
    m[i][j]=0
for i in range(n):
  for j in j1:
    m[i][j]=0
for i in range(n):
  print(*m[i])
