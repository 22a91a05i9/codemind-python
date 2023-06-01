n=int(input())
i=0
w=0
for i in range(n):
    a=int(input())
    w=a
    r=0;s=0
    while(a!=0):
        r=a%10
        s=s*10+r
        a=a//10
    if(w!=s):
        print("False")
    else:
        print("True")
        
    