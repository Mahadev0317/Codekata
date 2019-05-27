n=int(input())
lis=[];c=0
for i in range(n):
    row=list(map(int,input().split()))
    lis.append(row)
j=n-1
for i in range(n):
    c+=lis[i][j]
    j-=1
print(c)
