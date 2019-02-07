n=int(input())
li=list(map(int,input().split()))
s=0
if n<3:
  print(n)
else:
  for i in range(n+1):
    s+=i
  print(s)
