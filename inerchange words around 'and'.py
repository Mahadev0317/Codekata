li=list(input().split())
lis=[]
temp=""
if len(li)<3:
  print(*li)
else:
  for i in range(1,len(li)-1):
    if li[i]=="and":
      temp=li[i-1]
      li[i-1]=li[i+1]
      li[i+1]=temp
print(*li)
