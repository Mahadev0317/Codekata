n=int(input())
lis=[]
for i in range(n):
  li=list(map(int,input().split()))
  lis.extend(li)
print(*sorted(lis))
