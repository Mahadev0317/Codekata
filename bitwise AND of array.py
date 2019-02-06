n=int(input())
li=list(map(int,input().split()))
op=0
for i in range(n):
  for j in range(i+1,n):
    op+=(li[i] & li[j])
print(op)
