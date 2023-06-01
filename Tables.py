n,r=map(int,input().split())
for i in range(r+1):
    if(i%2==0):
        i=i+1
    else:
        print(n,"x",i,"=",n*i)