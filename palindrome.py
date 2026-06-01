a=int(input("Enter your number: "))
b=str(a)
c=b[::-1]   
if b==c:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")