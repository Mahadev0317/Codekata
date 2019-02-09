n=int(input())
li=list(map(int,input().split()))
op=[]
for i in range(1,len(li)):
  if li[i]%li[i-1]==0:
    op.append(li[i])
print(*op)
