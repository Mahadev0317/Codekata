n=int(input())
li=list(map(int,input().split()))
star=[];st=[]
f=0;a=0;l=0
for i in range(n):
  if i==n-1:
    st.append(li[i])
    l=1
  for j in range(i+1,n):
    if li[i]>li[j]:
      f=1
    else:
      break
  else:
    if i==0:
      st.append(li[i])
    elif f==1 and i!=0:
      st.append(li[i])
    if f==1 or l==1 and i>0:
      for k in range(0,i):
        if li[i]<=li[k]:
          break
      else:
        star.append(li[i])
    l=0
    f=0
print(*st)
print(*star)
