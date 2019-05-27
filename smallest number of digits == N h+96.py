n=int(input())
def sumofdigit(x):
    c=0
    for i in x:
        c+=int(i)
    return c
i=1

while i>0:
    if sumofdigit(str(i))==n:
        print(i)
        break
    i+=1
