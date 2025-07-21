num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choose = input("Choose the operation (+, =, *, /):")

match choose:
    case choose1:
        if choose == "+":
            results = num1+num2
            print(f"The result is {results}")
        elif choose == "-":
            results = num1-num2
            print(f"The result is {results}")
        elif choose == "*":
            results = num1*num2
            print(f"The result is {results}")
        elif choose == "/":
            results = num1/num2
            print(f"The result is {results}")
        else:
            print("sorry")

                