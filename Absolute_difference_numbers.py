n,x=map(int,input().split())
n=str(n)
f=int(n[:x])
l=int(n[-x:])
print(abs(f-l))
