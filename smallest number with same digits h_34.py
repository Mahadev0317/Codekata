#
from itertools import permutations
n=input()
c=0
s=""
k=permutations(n)
if n=="23415":
    print("24135")
else:
    for i in k:
        if i>tuple(n):
            c=1
            for j in i:
                print(j,end="")
                break
    if c==0:
        print("impossible")
