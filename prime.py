num = int(input("enter a number"))
count=0
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2,num):
        if (num %i)==0:
            count=1
            break
        if count == 1:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")