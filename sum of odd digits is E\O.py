li=list(input())
lis=[]
for i in li:
  if int(i)%2!=0:
    lis.append(int(i))
if sum(lis)%2==0:
  print("E")
else:
  print("O")
