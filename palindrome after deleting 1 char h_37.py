s=input()
def func(x,k):
    temp=""
    for i in range(len(x)):
        if i!=k:
            temp+=x[i]
    return temp

for i in range(len(s)):
    st=func(s,i)
    if st==st[::-1]:
        print("YES")
        break
else:
    print("NO")
