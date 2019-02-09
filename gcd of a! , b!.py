m,n=map(int,input().split())
def fact(x):
  if x==0 or x==1:
    return 1
  else:
    return x*fact(x-1)
m=fact(m)
n=fact(n)
for i in range(1,max(n,m)):
  if n%i==0 and m%i==0:
    k=i
else:
  print(k)
