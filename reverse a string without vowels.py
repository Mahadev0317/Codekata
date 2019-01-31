n=int(input())
s=input()
v=("A","a","E","e","I","i","O","o","U","u")
s1=""
for i in s:
  if i not in v:
    s1+=i
print(s1[::-1])
