#write a program to check if the number is palindrome or not
n=int(input("enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("the number is a palindrome")
else:
    print("the number isn't a palindrome")