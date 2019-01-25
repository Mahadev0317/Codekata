n=list(input())
lis=[]
for i in range(len(n)):
    if int(n[i])%2!=0:
        lis.append(n[i])
for i in range(len(lis)-1):
    print(lis[i],end=' ')
print(lis[len(lis)-1])
