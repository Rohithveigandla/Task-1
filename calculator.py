def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def main():
    while True:
        print("\n=== Simple CLI Calculator ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        choice = input("Choose an operation (1-5): ")
        if not choice.isdigit() or int(choice) not in range(1, 6):
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        choice = int(choice)
        if choice == 5:
            print("Exiting calculator. Goodbye!")
            break
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        if choice == 1:
            result = add(num1, num2)
            print(f"Result: {result:.2f}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"Result: {result:.2f}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"Result: {result:.2f}")
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = divide(num1, num2)
                print(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()
