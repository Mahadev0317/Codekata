n=int(input())
li=list(map(int,input().split()))
d=2
f=0
while 1:
  for i in li:
    if d%i!=0:
      f=1
      d+=1
      break
  else:
    f=0
  if f==0:
    break
print(d)
