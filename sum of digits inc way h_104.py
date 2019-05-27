n=input()
i=0;k=0
def sumofdigit(x):
    s=0
    for i in x:
        s+=int(i)
    return s
for j in range(1,len(n)+1):
    k+=sumofdigit(n[i:j])
print(k)
