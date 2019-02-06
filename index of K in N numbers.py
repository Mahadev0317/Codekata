n,k=map(int,input().split())
lis=list(map(int,input().split()))
for i in range(len(lis)):
  if lis[i]==k:
    print(i+1)
    break
