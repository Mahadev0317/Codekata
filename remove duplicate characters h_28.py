s=list(input())
li=[]
for i in s:
  if i not in li:
    li.append(i)
print("".join(li))
