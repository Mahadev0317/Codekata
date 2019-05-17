n=int(input())
c=0
def occ(x):
  d=0
  for i in x:
    if i=="2":
      d+=1
  return d
for i in range(n+1):
  c+=occ(str(i))
print(c)
