li=list(input())
c=0;m=0;f=0;i=0
while i<len(li):
  if li[i]=="a" and f==0:
    c+=1
    f=1
    i+=1
  elif li[i]=="b" and f==1:
    c+=1
    f=0
    i+=1
  else:
    if c>m:
      m=c
      c=0
    if li[i]!="a":
      i+=1
    c=0
    f=0
print(0 if m==1 else m)
