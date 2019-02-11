n=int(input())
li=sorted(list(map(int,input().split())))
lis=[i for i in range(1,n+1)]
for i in range(n):
  if li[i]!=lis[i]:
    print("no")
    break
else:
  print("yes")
