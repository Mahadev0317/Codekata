input()
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
for i in range(len(li2)):
  if(li2[i]) not in li1:
    print("NO")
    break
else:
  print("YES")
