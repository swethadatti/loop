n=int(input("enter the number"))
s=1
i=1
while i<=n:
    j=1
    while j<=i:
        print(s*s,end=" ")
        s=s+1
        j=j+1
    print()
    i=i+1