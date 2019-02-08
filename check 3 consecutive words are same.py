n=int(input())
li=[]
for i in range(n):
  li.append(input())
li=sorted(li)
for i in range(len(li)-2):
  if li[i]==li[i+1]==li[i+2]:
    print("yes")
    break
else:
  print("no")
