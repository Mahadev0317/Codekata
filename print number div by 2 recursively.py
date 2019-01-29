n=int(input())
if n%2!=0:
    print(n)
else:
    while(n>0):
        if n%2==0:
            print(int(n/2))
            n=int(n/2)
        else:
            break
