a=input()
b=input()
import sys
if len(a)>len(b):
  print(1)
  sys.exit(0)
A=[]
s=''
for i in range(len(a)):
  if a[i] not in A:
    s+=a[i]
    A.append(a[i])
c=0
c=len(a)//len(s)
d=1
for i in range(2,c+1):
  if c%i==0:
    d+=1
print(d)
#
