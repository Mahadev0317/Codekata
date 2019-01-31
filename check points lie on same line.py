li=[]
lis=[]
for i in range(3):
  n,k=map(int,input().split())
  li.append(n)
  lis.append(k)
if li[0]==li[1]==li[2] or lis[0]==lis[1]==lis[2]:
  print("yes")
elif li[0]==lis[0] and li[1]==lis[1] and li[2]==lis[2]:
  print("yes")
else:
  print("no")
