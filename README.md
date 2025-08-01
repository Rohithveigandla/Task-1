This Python program is a Command-Line Interface (CLI) calculator that allows users to perform four basic arithmetic operations:
Addition
Subtraction
Multiplication
Division

The calculator runs in a loop, continuously displaying a menu and prompting the user to select an operation until they choose to exit.

🔍 Key Features:
✅ User-Friendly Menu
Displays numbered options for arithmetic operations and an exit option.

Accepts user input to select an operation.

✅ Input Validation
Validates that the user's menu choice is a digit and within the range 1–5.

Validates number inputs using try-except to catch invalid entries (like letters or symbols).

✅ Arithmetic Operations
Defined using separate functions for modularity and clarity:
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)

The appropriate function is called based on the user's choice.

✅ Error Handling
Handles non-numeric input using try-except.

Prevents division by zero with a conditional check.

✅ Exit Option
Selecting option 5 cleanly exits the loop and ends the program with a farewell message.

💻 Example Usage:

=== Simple CLI Calculator ===
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
Choose an operation (1-5): 2
Enter first number: 10
Enter second number: 3
Result: 7.00



