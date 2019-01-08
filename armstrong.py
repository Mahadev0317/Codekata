n=input()
li=list(n)
l=len(li)
sum=0
for i in range(len(li)):
  sum+=(int(li[i])**l)
if sum==int(n):
  print("yes")
else:
  print("no")
