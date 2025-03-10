'''Instructions:
Basic Calculator Program
Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.'
'''
print("Calculator in Python")
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 -  num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid Operation."

num1 = float(input("Enter the First Number"))
num2 = float(input("Enter the second number"))
operation = input("Enter the Operation:")
result  = calculate(num1, num2, operation)
print(f"{num1} {operation} {num2} = {result}")