n=int(input())
def fib(x):
  if x<=1:
    return x
  else:
    return fib(x-1) + fib(x-2)
for i in range(1,n):
  print(fib(i),end=" ")
print(fib(n))
