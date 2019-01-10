x,y=map(int,input().split())
x,y = (x^y)^((x^y)^y),(x^y)^y
print(x,y)
