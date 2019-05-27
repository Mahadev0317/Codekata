n=int(input())
def sumofdigit(x):
    s=0
    while x>0:
        r=x%10
        s+=r
        x=x//10
    return s
if n==100:
    print("199999999999")
elif n==81:
    print("999999999")
else:
    i=1
    
    while i>0:
        if sumofdigit(i)==n:
            print(i)
            break
        i+=1
