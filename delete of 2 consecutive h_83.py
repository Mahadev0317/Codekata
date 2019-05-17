s=list(input())
op=[]
for i in range(len(s)-1):
  if (s[i]==s[i+1]):
    temp=[i for i in s]
    temp.pop(i+1)
    op.append("".join(temp))
max=int(op[0])
for i in range(1,len(op)):
  if(int(op[i])>max):
    max=op[i]
print(max)
