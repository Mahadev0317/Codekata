n,k=map(int,input().split())
n=list(map(int,input().split()))
k=list(map(int,input().split()))
lis=[]
for i in k:
  n.append(i)
  lis.append(max(n))
print(*lis)
