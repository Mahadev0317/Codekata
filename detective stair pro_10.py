n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n):
    if a[i-1]<a[i]:
        c+=sum(a[:i])
    else:
        for j in range(0,i):
            if a[j]<a[i]:
                c+=a[j]
print(c)
