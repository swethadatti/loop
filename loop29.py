i=1
while i<=5:
    j=1
    while j<=i:
        if i==2 or i==4:
            print("*",end=" ")
            j=j+1
        else:
             print(j,end=" ")
        j=j+1
    print()
    i=i+1