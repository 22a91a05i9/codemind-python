n=int(input())
s=0
if(n<0):
    n=(-1)*n
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    print(-s)
else:
    while(n>0):
        r=n%10 
        s=s*10+r
        n=n//10
    print(s)

