n,k=map(int,input().split())
for i in range(n):
  if (k**i)==n:
    print("yes")
    break
else:
  print("no")
