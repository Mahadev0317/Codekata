n,k=map(int,input().split())
lis=list(map(int,input().split()))
s=0
for i in range(0,k):
  s+=lis[i]
print(s)
