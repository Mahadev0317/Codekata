from itertools import combinations
n,k=input().split()
if int(k)==0:
    print(n)
else:
    a=list(combinations(n,len(n)-int(k)))
    op=[int("".join(i)) for i in a]
    print(min(op))
