n=int(input())
for i in range(n,0,-1):
    if not (i&(i-1)):
        print(n-i)
        break
#Helloo
