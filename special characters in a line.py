n=list(input())
c=0
for i in n:
  if not i.isalnum():
    if i!=" ":
      c+=1
print(c)
