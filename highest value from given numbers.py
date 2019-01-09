int(input())
li=sorted(list(map(int,input().split())))
lis=li[::-1]
if lis[0]!=0:
  for i in range(len(lis)):
    print(lis[i],end="")
else:
  print(0)
