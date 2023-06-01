n=int(input())
sq=n*n
temp=n
c=1
while(n!=0):
    n=n//10
    c=c*10
if(sq%c==temp):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
