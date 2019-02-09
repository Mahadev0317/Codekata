a,b=input().split()
n=sorted(set(a))
k=sorted(set(b))
if len(n)==len(k):
  for i in range(len(n)):
    if n[i]!=n[i]:
      print("false")
      break
  else:
    print("true")
else:
  print("false")
