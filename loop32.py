n=int(input("enter the number"))
i=1
while i<=n:
    if i%3==0 and i%7==0:
        print ("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print ("gurukul")
    else:
         print(i)
    i=i+1