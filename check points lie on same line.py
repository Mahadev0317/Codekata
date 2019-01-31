li=[]
lis=[]
for i in range(3):
  n,k=map(int,input().split())
  li.append(n)
  lis.append(k)
if li[0]==li[1]==li[2] or lis[0]==lis[1]==lis[2]:
  print("yes")
else:
  print("no")
