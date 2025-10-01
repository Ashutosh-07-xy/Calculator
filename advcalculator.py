import math

# --- BASIC ARITHMETIC FUNCTIONS (Binary Operations) ---

def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y (x - y)."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y (x / y). Handles division by zero."""
    if y == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return x / y

def power(x, y):
    """Returns x raised to the power of y (x^y)."""
    return x ** y

# --- SCIENTIFIC FUNCTIONS (Unary Operations) ---

def sin_deg(x):
    """Returns the sine of x, assuming x is in degrees."""
    return math.sin(math.radians(x))

def cos_deg(x):
    """Returns the cosine of x, assuming x is in degrees."""
    return math.cos(math.radians(x))

def tan_deg(x):
    """Returns the tangent of x, assuming x is in degrees."""
    # Check for values near 90 + 180k degrees where tan is undefined
    if abs((x - 90) % 180) < 1e-9:
        return "Error: Tangent is undefined for this degree (approaching $\\pm\\infty$)."
    return math.tan(math.radians(x))

def natural_log(x):
    """Returns the natural logarithm (log base e) of x."""
    if x <= 0:
        raise ValueError("Error: Natural logarithm is only defined for positive numbers ($x > 0$).")
    return math.log(x)

def log_base10(x):
    """Returns the logarithm base 10 of x."""
    if x <= 0:
        raise ValueError("Error: Logarithm base 10 is only defined for positive numbers ($x > 0$).")
    return math.log10(x)

def exponential(x):
    """Returns $e$ raised to the power of x ($e^x$)."""
    return math.exp(x)

# --- OPERATION MAPPINGS AND MENU ---

# Operations requiring two operands (x, y)
BINARY_OPERATIONS = {
    "+": {"func": add, "name": "Addition"},
    "-": {"func": subtract, "name": "Subtraction"},
    "*": {"func": multiply, "name": "Multiplication"},
    "/": {"func": divide, "name": "Division"},
    "^": {"func": power, "name": "Power ($x^y$)"},
}

# Operations requiring one operand (x)
UNARY_OPERATIONS = {
    "sin": {"func": sin_deg, "name": "Sine (Degrees)"},
    "cos": {"func": cos_deg, "name": "Cosine (Degrees)"},
    "tan": {"func": tan_deg, "name": "Tangent (Degrees)"},
    "ln": {"func": natural_log, "name": "Natural Log ($log_e$)"},
    "log10": {"func": log_base10, "name": "Log Base 10"},
    "exp": {"func": exponential, "name": "Exponential ($e^x$)"},
}

def print_menu():
    """Displays the calculator menu options."""
    print("\n--- Scientific Calculator Menu ---")
    print("\nBasic Operations (Requires two numbers):")
    for symbol, details in BINARY_OPERATIONS.items():
        print(f"  '{symbol}': {details['name']}")

    print("\nScientific Functions (Requires one number):")
    for command, details in UNARY_OPERATIONS.items():
        print(f"  '{command}': {details['name']}")

    print("\nCommands:")
    print("  'menu': Show this menu")
    print("  'quit': Exit the calculator")
    print("----------------------------------")

# --- MAIN CALCULATOR LOOP ---

def calculator():
    """The main function to run the interactive calculator."""
    print("Welcome to the Python Scientific Calculator.")
    print_menu()

    while True:
        choice = input("\nEnter operation command (e.g., '+', 'sin', 'quit', 'menu'): ").lower().strip()

        if choice == 'quit':
            print("Exiting calculator. Goodbye!")
            break
        elif choice == 'menu':
            print_menu()
            continue
        
        try:
            if choice in BINARY_OPERATIONS:
                # Handle Binary Operations (e.g., +, *, ^)
                num1 = float(input(f"Enter the first number (x): "))
                num2 = float(input(f"Enter the second number (y): "))

                operation_details = BINARY_OPERATIONS[choice]
                result = operation_details['func'](num1, num2)
                
                # Check for floating point results that are effectively integers
                if abs(result - round(result)) < 1e-9:
                    result = int(round(result))
                    
                print(f"Result of {operation_details['name']}: {num1} {choice} {num2} = {result}")

            elif choice in UNARY_OPERATIONS:
                # Handle Unary Operations (e.g., sin, ln, exp)
                num = float(input(f"Enter the number (x): "))
                
                operation_details = UNARY_OPERATIONS[choice]
                result = operation_details['func'](num)

                # Special handling for error message from tan_deg
                if isinstance(result, str) and result.startswith("Error:"):
                    print(result)
                    continue

                # Check for floating point results that are effectively integers
                if abs(result - round(result)) < 1e-9:
                    result = int(round(result))
                
                print(f"Result of {operation_details['name']} on {num}: {result}")

            else:
                print("Invalid command. Please enter a valid operation symbol or 'menu'.")

        except ValueError as e:
            # Catches errors if the user enters non-numeric input when asked for a number
            print(f"Invalid numeric input. Please ensure you enter valid numbers. ({e})")
        except ZeroDivisionError as e:
            # Catches the specific division by zero error
            print(f"{e}")
        except Exception as e:
            # Catches other unexpected math errors (e.g., negative number for sqrt or power)
            print(f"A mathematical error occurred: {e}")


if __name__ == "__main__":
    calculator()
