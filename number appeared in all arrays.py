n,m=map(int,input().split())
lis=[list(map(int,input().split())) for i in range(n)]
opt=[]
for i in range(m):
  for j in range(1,len(lis)):
    if lis[0][i] not in lis[j]:
      break
  else:
    opt.append(lis[0][i])
op=sorted(opt)
for i in range(len(op)-1):
  print(op[i],end=" ")
print(op[len(op)-1])
