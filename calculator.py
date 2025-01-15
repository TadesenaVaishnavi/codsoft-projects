#calculator
def calculator():
    print("Welcome to the Continuous Calculator!")
    result = None

    while True:
        try:
            if result is None:
                num1 = float(input("Enter the first number: "))
            else:
                num1 = result

            operation = input("Enter the operation (+, -, *, /): ")
            num2 = float(input("Enter the next number: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            else:
                print("Invalid operation. Please choose +, -, *, or /.")
                continue

            print(f"The result is: {result}")

            # Ask user if they want to continue or exit
            choice = input("Do you want to continue with this result? (yes/no): ").strip().lower()
            if choice != "yes":
                print("Exiting the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numerical values.")

# Run the calculator
calculator()