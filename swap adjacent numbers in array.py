n=int(input())
li=list(map(int,input().split()))
lis=[]
for i in range(n):
  if i%2==0:
    lis.insert(i+1,li[i])
  else:
    lis.insert(i-1,li[i])
print(*lis)
