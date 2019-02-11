n=input()
x=int(n,2)
while 1:
  if (x & (x-1)):
    x+=1
  else:
    print(x)
    break
