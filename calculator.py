num=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
symbol=input("Enter the symbol for the operation you want to perform (+, -, *, /,%,**): ")

if symbol == "+":
    print("The sum of the numbers is: ", num + num2)
elif symbol == "-":
    print("The difference of the numbers is: ", num - num2)
elif symbol == "*":
    print("The product of the numbers is: ", num * num2)
elif symbol == "/":
    print("The quotient of the numbers is: ", num / num2)
elif symbol == "%":
    print("The remainder of the numbers is: ", num % num2)
elif symbol == "**":
    print("The result of the exponentiation is: ", num ** num2)
else:
    print("Invalid symbol entered.")
