i=1
n=6
sum=0
while i<=n:
    if n%i==0:
        sum=sum+i
    i=i+1
    if(sum==n):
        print("perfect no")
    else:
         print("not")