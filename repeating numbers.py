n=int(input())
li=list(map(int,input().split()))
lis=[0]*10
for i in range(len(li)):
  lis[li[i]]+=1
op=[]
for i in range(len(lis)):
  if lis[i]>1:
    op.append(i)
if len(op)!=0:
  for i in range(len(op)-1):
    print(op[i],end=" ")
  print(op[len(op)-1])
else:
  print("unique")
