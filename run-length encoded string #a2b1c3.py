li=list(input())
lis=[]
for i in range(1,len(li),2):
  lis.append(li[i-1]*int(li[i]))
print("".join(lis))
