n=int(input())
temp=[];op=[]
def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True
for i in range(2,100):
    if prime(i):
        temp.append(i)
for i in range(len(temp)-2):
    for j in range(i+1,len(temp)-1):
        for k in range(j+1,len(temp)):
            if (temp[i]+temp[j]+temp[k])==n:
                op.append([temp[i],temp[j],temp[k]])
print(*op[0])
