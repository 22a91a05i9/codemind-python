n=int(input())
for i in range(0,n):
    if(i*(i+1)==n):
        break;
if(n==i*(i+1)):
    print("YES")
else:
    print("NO")
