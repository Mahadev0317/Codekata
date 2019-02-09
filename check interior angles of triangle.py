a,b,c=map(int,input().split())
if a==0 or b==0 or c==0:
  print("no")
else:
  if a+b+c==180:
    print("yes")
  else:
    print("no")
