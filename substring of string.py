n,m=input().split()
for i in range(len(n)-1):
  if n[i:i+len(m)]==m:
    print("yes")
    break
else:
  print("no")
