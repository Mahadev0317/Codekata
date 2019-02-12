n=int(input())
li=list(map(int,input().split()))
op=li
def even(x):
  lis=[]
  for i in range(1,len(x),2):
    lis.append(x[i])
  return lis
while len(li)!=1:
  li=even(li)
print(op.index(li[0]))
