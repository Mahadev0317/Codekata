n=int(input())
temp=[]
def prime(x):
  for i in range(2,x):
    if x%i==0:
      return False
  else:
    return True

for i in range(2,n):
  if prime(i) is True:
    temp.append(i)
if len(temp) is 0:
  print(0)
else:
  for i in range(len(temp)-1):
    print(temp[i],end=" ")
  print(temp[len(temp)-1])
