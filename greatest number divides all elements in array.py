n=int(input())
li=list(map(int,input().split()))
for i in li:
  if i%2!=0:
    print(1)
    break
else:
  print(2)
