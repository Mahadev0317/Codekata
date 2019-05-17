s=list(map(str,input().split("#")))
s1=list(map(str,input().split("#")))
def func(arr):
  x=0
  for i in range(1,4):
    x+=int(arr[i])
  return x
print(s[0] if func(s)>func(s1) else s1[0])
