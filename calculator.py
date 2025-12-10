def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            #Allow exiting during number entry
            if value.lower() in ["quit", exit]:
                return None
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def calculate(num1, operator, num2): 
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result =  num1 - num2
    elif operator == "*":
        result =  num1 * num2
    elif operator == "/":
        if num2 != 0:
            result =  num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operator!"
    
    # Display integer results cleanly
    if result.is_integer():
        return int(result)
    else:
        return round(result, 5) # Limit decimal places
    
def main():
    print("Welcome to the Python Calculator!")
    print("Operations: +, -, *, /")
    print("Type 'quit' anytime to exit.\n")
    
    
    while True:
        num1 = get_number("Enter first number (or 'quit'): ")
        if num1 is None:
            print("Goodbye!")
            break

        operator = input("Enter operation (+, -, *, /): ")
        if operator.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        num2 = get_number("Enter second number (or 'quit'): ")
        if num2 is None:
            print("Goodbye!")
            break
    
        result = calculate(num1, operator ,num2)
        print(f"\n-> {num1} {operator} {num2} = {result}\n")
    
    
    print(f"{num1} {operator} {num2}")
    
if __name__ == "__main__":
    main()