int(input())
lis=list(map(int,input().split()))
li=[]
for i in lis:
  if i not in li:
    li.append(i)
  else:
    print(i)
    break
else:
  print("unique")
