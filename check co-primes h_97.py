n,m=map(int,input().split())
temp=[]
def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True
for i in range(2,1000):
    if prime(i):
        temp.append(i)
if n in temp and m in temp:
    print("yes")
else:
    print("no")
