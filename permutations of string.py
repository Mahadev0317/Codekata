from itertools import permutations
n=list(input())
pe=permutations(n)
p=[]
for i in pe:
  if i not in p:
    p.append(i)
for i in range(len(p)-1):
  print("".join(p[i]),end="\n")
print("".join(p[len(p)-1]))
