li=list(map(int,input().split()))
lis=[]
for i in range(len(li)):
  if i%2!=0:
    if li[i]%2==0:
      lis.append(li[i])
  else:
    if li[i]%2!=0:
      lis.append(li[i])
for i in range(len(lis)-1):
  print(lis[i],end=" ")
print(lis[len(lis)-1])
