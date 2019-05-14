n,t,k=map(int,input().split())
arr=list(map(int,input().split()))
temp=[]
def func(arr):
  if len(arr) == 1:
    return
  else:
    for i in range(len(arr)):
      arr1=arr.copy()
      arr1.pop(i)
      if arr1 not in temp:
        temp.append(arr1)
      func(arr1)
func(arr)
for i in temp:
  if len(i)==t and sum(i)==k:
    f=1
else:
  if f==1:
    print("YES")
  else:
    print("NO")
