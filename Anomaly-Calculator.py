print("welcome to AnomalyCalculator!")
print("1. Addition!")
print("2. Subtraction!")
print("3. Multiplication!")
print("4. Division!")
choice = input("Choose an option: ")

if choice == "1":
    print("You chose Addition!")
    
    number1 = int(input("Enter the first number: "))
    number2 =int(input("Enter  the second number: "))
    result = number1 + number2
    print("Result: ", result)

if choice == "2":
    print("you chose Subtraction!")

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = number1 - number2
    print("REsult: ", result)

if choice == "3":
    print("You chose Multiplication!")

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = number1 * number2
    print("Result: ", result)

if choice == "4":
    print("You chose Division!")

    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = number1 / number2
    print("Result: ", result)