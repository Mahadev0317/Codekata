n=int(input())
li=list(map(int,input().split()))
lis=[]
for i in range(len(li)-1):
  lis.append(li[i]+li[i+1])
print(sum(lis))
