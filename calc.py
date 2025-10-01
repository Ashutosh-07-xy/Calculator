# Simple Command-Line Calculator

# --- Arithmetic Functions ---

def add(num1, num2):
    """Adds two numbers and returns the result."""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts the second number from the first and returns the result."""
    return num1 - num2

def multiply(num1, num2):
    """Multiplies two numbers and returns the result."""
    return num1 * num2

def divide(num1, num2):
    """Divides the first number by the second. Handles division by zero."""
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2

# Dictionary to map operation symbols to their respective functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# --- Main Calculator Logic ---

def calculator():
    """Runs the main calculator loop."""
    print("Welcome to the Simple Python Calculator!")
    print("Available operations:")
    for symbol in operations.keys():
        print(f"  {symbol}")
    print("Type 'quit' to exit.")

    while True:
        try:
            # 1. Get the first number
            num1_input = input("\nEnter the first number: ")
            if num1_input.lower() == 'quit':
                break
            num1 = float(num1_input)

            # 2. Get the operation symbol
            operation_symbol = input("Enter the operation (+, -, *, /): ")
            if operation_symbol.lower() == 'quit':
                break

            if operation_symbol not in operations:
                print("Invalid operation symbol. Please try again.")
                continue

            # 3. Get the second number
            num2_input = input("Enter the second number: ")
            if num2_input.lower() == 'quit':
                break
            num2 = float(num2_input)

            # 4. Perform calculation and get the function
            calculation_function = operations[operation_symbol]
            result = calculation_function(num1, num2)

            # 5. Display result
            print(f"\nResult: {num1} {operation_symbol} {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            # Catch any unexpected errors
            print(f"An unexpected error occurred: {e}")

    print("\nThank you for using the calculator. Have a nice day!")

# Execute the main calculator function
if __name__ == "__main__":
    calculator()
