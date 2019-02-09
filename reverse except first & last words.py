li=list(input().split())
lis=[]
for i in range(0,len(li)):
  if i==0:
    lis.append(li[i])
  elif i in range(1,len(li)-1):
    lis.append(li[i][::-1])
  elif i==len(li)-1:
    lis.append(li[i])
print(*lis)
