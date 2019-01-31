n,k=map(int,input().split())
j=max(n,k)
while 1:
  if j%n==0 and j%k==0:
    print(j)
    break
  j+=1
