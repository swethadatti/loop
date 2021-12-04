n=int(input("enter the number"))
i=2
while i<=n:
    count=0
    j=2
    while j<i:
        if i%j==0:
            count=count+1
        j=j+2
    if count==0:
        print(i,"prime number")
    i=i+3



