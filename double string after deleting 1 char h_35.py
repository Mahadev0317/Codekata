s=input()
def func(x,k):
    temp=""
    for i in range(len(x)):
        if i!=k:
            temp+=x[i]
    return temp

def doublestr(x):
    l=len(x)//2
    if x[:l]==x[l:]:
        return True
    else:
        return False
    
for i in range(len(s)):
    st=func(s,i)
    if doublestr(st):
        print("YES")
        break
else:
    print("NO")
