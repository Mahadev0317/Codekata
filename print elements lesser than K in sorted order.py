n,k=map(int,input().split())
l=list(map(int,input().split()))
lis=[]
for i in l:
  if i<k:
    lis.append(i)
print(*sorted(lis))
