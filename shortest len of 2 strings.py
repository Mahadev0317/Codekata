n,k=input().split()
if len(n)<len(k):
  print(n)
elif len(n)>len(k):
  print(k)
else:
  if len(n)//2==1:
    print(n)
  else:
    print(k)
