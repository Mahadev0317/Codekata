lis=list(input())
for i in range(0,len(lis),2):
  lis[i],lis[i+1]=lis[i+1],lis[i]
print("".join(lis))
