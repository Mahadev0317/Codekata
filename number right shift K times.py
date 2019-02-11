n,k=map(int,input().split())
s=bin(n)[2:]
s=list(s)
for i in range(k):
  s.pop()
  s.insert(0,"0")
b="".join(s)
op=int(b,2)
print("{:.2f}".format(op))
