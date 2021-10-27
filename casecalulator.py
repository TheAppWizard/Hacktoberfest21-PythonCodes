# Simple Calculator Python
# Enter Choice
# 1.Add 2.Subtract 3. Multiply 4.Divide ('1', '2', '3', '4')
# Enter Two Values
# Get Answer
# Next Calculation : (yes/no)

# ----------------------------------

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            try:
                print(num1, "/", num2, "=", divide(num1, num2))
            expect ZeroError:
                print("enter a valid inputs, division by zero is invalid")
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

# ----------------------------------


operator = input("Enter the operation: add, subtract, divide, multiply").lower()

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

if operator == 'add':
    output = num1 + num2
    print(output)

elif operator == 'subtract':
    output = num1 - num2
    print(output)

elif operator == 'divide':
    output = num1/num2
    print(output)
    
elif operator == 'multiply':
    output = num1 * num2
    print(output)
