#
n=int(input())
li=list(map(int,input().split()))
lis=sorted(li)
for i in range(len(lis)-1):
  print(lis[i],end=" ")
print(lis[len(lis)-1])
