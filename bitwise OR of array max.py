n=int(input())
li=list(map(int,input().split()))
lis=[]
for i in range(n-1):
  lis.append(li[i]|li[i+1])
print(max(lis))
#hello
