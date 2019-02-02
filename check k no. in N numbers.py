n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in l:
  if k==i:
    print("yes")
    break
else:
    print("no")
