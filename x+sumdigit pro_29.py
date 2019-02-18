n=int(input())
def sumdigit(x):
    x=str(x);s=0
    for i in x:
       s+=int(i)
    return s
op=[]
for i in range(n):
    if (n==i+sumdigit(i)):
        op.append(i)
print(len(op))
for i in op:
    print(i)
