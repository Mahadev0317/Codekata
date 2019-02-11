from itertools import permutations
n=list(input())
p=permutations(n)
for i in set(p):
  print("".join(i))
