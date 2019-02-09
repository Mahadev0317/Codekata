n,k=map(int,input().split())
def fact(x):
  if x==0 or x==1:
    return 1
  else:
    return x*fact(x-1)
print(fact(n)//(fact(k)*fact(n-k)))
