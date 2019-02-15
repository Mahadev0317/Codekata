n=int(input())
a=list(map(int,input().split()))
for i in range(1,n-1):
  if sum(a[0:i])//len(a[0:i])==sum(a[i:n])//len(a[i:n]):
    print("yes")
    break
else:
  print("no")
