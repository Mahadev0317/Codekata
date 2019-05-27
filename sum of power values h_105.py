n=input()
if len(n)==1:
    print(n)
else:
    s=0
    for i in range(len(n)):
        s+=(int(n[i])**int(n[-1]))
    print(s)
