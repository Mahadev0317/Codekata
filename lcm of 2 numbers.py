m,n=map(int,input().split())
n1=min(m,n)
while(1):
  if n1%m==0 and n1%n==0:
    print(n1)
    break
  n1+=1
