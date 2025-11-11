from functions import add, subtract, multiply, divide

def get_choice():
    """Prompt user for operation choice and validate input."""
    while True:
        print("\nSelect your choice:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        choice = (input("\nEnter your choice (1-5): "))
        if choice in ["1", "2", "3", "4", "5"]:
            return int(choice)
        print("Invalid input. Please enter a number between 1 and 5")
        
def get_number(prompt):
    """Prompt user for a number and validate input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate(choice, num1, num2):
    """Perform calculation based on choice."""
    try:
        if choice == 1:
            return add(num1, num2)
        elif choice == 2:
            return subtract(num1, num2)
        elif choice == 3:
            return multiply(num1, num2)
        elif choice == 4:
            return divide(num1, num2)
    except ZeroDivisionError:
        return "Error: cannot divide by zero."
    
def print_result(result):
    """Print result pretty."""
    if isinstance(result, str):
        print(result)
    else:
        if result == int(result):
            print("Result:", int(result))
        else:
            print(f"Result: {result:.2f}")

def run_calculator():
    """Main calculator loop."""
    while True:
        choice = get_choice()
        if choice == 5:
            print("Goodbye!")
            break
        num1 = get_number("Enter your first number: ")
        num2 = get_number("Enter your second number: ")
        result = calculate(choice, num1, num2)
        print_result(result)

# Run the calculator
if __name__ == "__main__":
    run_calculator()