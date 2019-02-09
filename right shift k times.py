n,k=map(int,input().split())
li=list(map(int,input().split()))
i=0
while i<k:
  li.insert(0,li[len(li)-1])
  li.pop()
  i+=1
print(*li)
