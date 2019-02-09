def prime(n):
  if n<2:
    print("no")
  else:
    for i in range(2,n):
      if n%i==0:
        print("no")
        break
    else:
      print("yes")
s=input()
li=[]
for i in s:
  if i!=" ":
    li.append(i)
prime(len(li))
