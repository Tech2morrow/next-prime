flag = 0

# Function
def nextprime(n,m):
    if n<2:
        print("2")
        exit()

    while True:
        n+=1
        for i in range(2,n):
            if n%i == 0:
                break

        else:
            global flag

            flag+=1
            if(flag==m):
                print("Next Prime : ",n)


try:
    x = int(input("Enter Number : "))

    nextprime(x,1)


except ValueError:
    print("Enter an integer")