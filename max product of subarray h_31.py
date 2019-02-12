n=int(input())
li=list(map(int,input().split()))
def prod(x):
  p=1
  for i in x:
    p*=i
  return p
m=max(li)
for i in range(1,n):
  for j in range(0,n):
    if i+j<=n:
      if prod(li[j:j+i])>m:
        m=prod(li[j:j+i])
print(m)
