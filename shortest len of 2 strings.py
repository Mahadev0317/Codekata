n,k=input().split()
if len(n) and len(k)==1:
  print(n)
else:
  if len(n)<len(k):
    print(n)
  elif len(n)>len(k):
    print(k)
  else:
    if len(n)//2==1:
      print(n)
    else:
      print(k)
