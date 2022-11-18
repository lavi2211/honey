n=int(input("enter a number for finding factors:"))
if(n<=0):
    print("{}is a invalid input:".format(n))
else:
    for i in range(1,n+1):
        if (n%i==0):
            print("\t{}".format(i))

















