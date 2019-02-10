n,k,m=map(int,input().split())
li=[]
li.append(n)
li.append(m)
li.append(k)
l=sorted(li)
if (l[0]**2)+(l[1]**2)==l[2]**2:
  print("yes")
else:
  print("no")
