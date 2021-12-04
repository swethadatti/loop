# num=int(input("enter the rows:"))
# for i in range(num,0,-1):
#     for j in range(0,num-i):
#         print(end=" ")
#     print()


# i=4
# while i>0:
#     j=1
#     while j<i:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i-1

i=4
s=1
while i>0:
    j=1
    while j<0:
        print(" "*s,i*"*"," "*s)
        j+=1
    i-=1
