n=int(input())
li=list(map(int,input().split()))
p=1
for i in li:
  p*=i
op=[]
for i in li:
  op.append(p//i)
print(*op)
