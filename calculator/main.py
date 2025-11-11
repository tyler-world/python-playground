from functions import add, subtract, multiply, divide

print("Select your choice:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide\n")

choice = int(input("Select your choice (1-4): "))

if choice not in [1, 2, 3, 4]:
    result = ("Invalid input.")
else:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)
else:
    result = "Invalid input."

if isinstance(result, str):
    print(result) # it's an error message
else:
    if result == int(result):
        print("Result: ", int(result)) # whole number, print as int
    else:
        print(f"Result: {result:.2f}") # decimal number, print with 2 decimal places