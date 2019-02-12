n=int(input())
li=list(map(int,input().split()))
for i in range(0,n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      if (li[i]+li[j])==li[k]:
        print(li[i],li[j],li[k])
