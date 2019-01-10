int(input())
lis=list(map(int,input().split()))
if len(lis)==1:
  print(lis[0],lis[0])
else:
  print(min(lis),max(lis))
