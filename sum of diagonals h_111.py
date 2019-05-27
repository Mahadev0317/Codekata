n=int(input())
lis=[];c=0
for i in range(n):
    row=list(map(int,input().split()))
    lis.append(row)
for i in range(n):
    c+=lis[i][i]
print(c)
