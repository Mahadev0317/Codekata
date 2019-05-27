n=int(input())
lis=list(map(int,input().split()))
for i in range(n):
   if sum(lis[:i])==sum(lis[i+1:]):
      print("yes")
      break
else:
   print("no")
