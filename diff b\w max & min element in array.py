n=int(input())
l=list(map(int,input().split()))
li=[]
for i in l:
  if i!=0:
    li.append(i)
a=min(li)
b=max(li)
print(b-a)
