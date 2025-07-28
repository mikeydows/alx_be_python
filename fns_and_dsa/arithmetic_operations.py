def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1+num2
        case "subtract":
            return num1-num2
        case "multiply":
            return num1*num2
        case "divide":
            if num2 == 0:
                print(f"you can't divide {num1} by {num2}")
            else:
                return num1/num2
        case _:
            print(f"{operation}, wrong operation try again")
