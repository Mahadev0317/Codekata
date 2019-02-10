n=int(input())
li=list(map(int,input().split()))
lis=list(map(int,input().split()))
k=n-1
for i in range(n):
  if li[i]!=lis[k]:
    print("no")
    break
  k-=1
else:
  print("yes")
