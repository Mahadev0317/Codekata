n=list(map(str,input().split()))
temp=[]
for i in n:
  temp.append(i[::-1])
print(*temp)
