li=list(input())
lis=[]
for i in li:
  if i not in lis:
    lis.append(i)
print("".join(lis))
