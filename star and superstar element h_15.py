n=int(input())
li=list(map(int,input().split()))
star=[];st=[]
for i in range(n):
  for j in range(i+1,n):
    if li[i]<=li[j]:
      break
  else:
      st.append(li[i])
star.append(max(li))
print(*st)
print(*star)
