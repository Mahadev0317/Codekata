n,k=input().split()
li=list(n)
for i in li:
  if i>k:
    print("no")
    break
else:
  print("yes")
