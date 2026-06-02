a=float(input("Enter the price of the firstitem: "))
b=float(input("Enter the price of the second item: "))
c=float(input("Enter the price of the third item: ")) 
d=float(input("Enter the price of the fourth item: "))
e=float(input("Enter the price of the fifth item: "))
f=float(input("Enter the price of the sixth item: "))
g=float(input("Enter the price of the seventh item: "))
h=float(input("Enter the price of the eighth item: "))
i=float(input("Enter the price of the ninth item: ")) 
j=float(input("Enter the price of the tenth item: "))
total=a+b+c+d+e+f+g+h+i+j
discount=total*0.10
final_amount=total-discount
print("final amount of the bill: ", final_amount)       