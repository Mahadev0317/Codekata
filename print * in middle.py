n=list(input())
l=len(n)
s=''
if l%2==0:
    for i in range(0,l):
        if i==(l//2-1):
            s=s+'*'
        elif i==l//2:
            s=s+'*'
        else:
            s=s+n[i]
else:
    for i in range(0,l):
        if i==l//2:
            s=s+'*'
        else:
            s=s+n[i]
print(s)
