n=int(input())
s=list(map(int,input().split()))
p1=s[::2]
p2=s[1::2]
print(max(sum(p1),sum(p2)))
