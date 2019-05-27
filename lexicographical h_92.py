from itertools import permutations
s=input()
k=permutations(s)
l=[]
m=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==s:
  print(s)
elif s==a[::-1]:
  print("-1")
else:
	s=tuple(s)
	for i in k:
		l.append(i)
	for i in l:
		if i>s:
			m=i
			break

	for i in l:
		if i>s and i<m:
			m=i

	if m==-1:
		print("-1")
	else:
		for i in m:
			print(i,end="")
  ##
