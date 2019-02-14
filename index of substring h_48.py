li=input()
l=input()
n=len(l)
for i in range(len(li)-n+1):
  if li[i:i+n]==l:
    print(i)
    break
