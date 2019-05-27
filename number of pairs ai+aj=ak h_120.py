n=int(input())
lis=list(map(int,input().split()))
c=0
for i in range(len(lis)-2):
   for j in range(i+1,len(lis)-1):
      for k in range(j+1,len(lis)):
         print(lis[i],lis[j],lis[k])
         if lis[i]+lis[j]==lis[k]:
            c+=1
print(c)
