n=int(input())
li=list(map(int,input().split()))
lis=[]
neg=[];pos=[]
for i in li:
  if i<0:
    neg.append(i)
  else:
    pos.append(i)
neg=sorted(neg,reverse=True)
if len(pos)==0:
  print(max(li))
elif len(neg)==0:
  print(sum(pos))
else:
  print(sum(pos)+neg[0])
