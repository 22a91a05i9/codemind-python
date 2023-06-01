n=int(input())
sum=0
p=n*n
while(p!=0):
    d=p%10
    p=p//10
    sum=sum+d
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")


