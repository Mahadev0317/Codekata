n=int(input())
li=list(map(int,input().split()))
s=1
if n==1:
  s=li[0]
else:
  for i in range(len(li)-1):
    s*=(li[i]*li[i+1])
if s%2!=0:
  print("odd")
else:
  print("even")
