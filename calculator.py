#python simple calculator

operator = input("Enter an operator (+ - * /) :")
num1 = float(input("Enter the first Number :"))
num2 = float(input("Enter the second Number :"))

if operator == "+":
    result = num1+num2
    print(f"The result is {result}")
elif operator == "-":
    result = num1-num2
    print(f"result is {result}")
elif operator == "*":
    result = num1*num2
    print(f"result is {result}")
elif operator == "/":
    result = num1/num2
    print(f"result is {result}")
else :
    print("The Operator You Entered is Invalid")