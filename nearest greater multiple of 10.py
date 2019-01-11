n=int(input())
if n<10:
  print(10)
elif n%10==0:
  print(n)
elif n%10>5:
  l=n%10
  print(n+(10-l))
elif n%10<=5:
  k=n%10
  print(n-k)
