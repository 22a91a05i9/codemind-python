n=int(input())
i=0
while(True):
    if(2**i<n):
        i=i+1
        continue
    elif(2**i==n):
        print(0)
        break
    else:
        if(abs(n-(2**(i-1)))>abs(n-(2**(i)))):
            print(abs(n-(2**(i))))
            break
        else:
            print(abs(n-(2**(i-1))))
            break
