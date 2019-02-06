n=int(input())
l=list(map(int,input().split()))
lis=[]
for i in l:
  if i<n:
    lis.append(i)
print(*sorted(lis))
