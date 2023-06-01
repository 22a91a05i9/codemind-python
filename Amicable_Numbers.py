n=int(input())
m=int(input())
c=0
p=0
for i in range(1,n):
    if(n%i==0):
        c+=i
for i in range(1,m):
    if(m%i==0):
        p+=i
if(n==p and m==c):
    print("Amicable")
else:
    print("Not Amicable")
