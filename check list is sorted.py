n=int(input())
lis=list(map(int,input().split()))
li=sorted(lis)
if lis==li:
  print("yes")
else:
  print("no")
