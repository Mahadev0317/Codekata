n,k,m=map(int,input().split())
if (n+m)>k and (n+k)>m and (m+k)>n:
  print("yes")
else:
  print("no")
