s=list(input())
v=["a","e","i","o","u"]
li=['v' if i in v else 'c' for i in s]
c=1
lis=[]
for i in range(len(li)-1):
  if li[i]=="v" and li[i+1]=="c" or li[i]=="c" and li[i+1]=="v":
    c+=1
  else:
    lis.append(c)
    c=1
lis.append(c)
print(0 if max(lis)==1 else max(lis))
