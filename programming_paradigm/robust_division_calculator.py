def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            raise ZeroDivisionError

        result = num / denom
        print(f"Result: {result}")

    except ValueError:
        print("Error: Both inputs must be numeric.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

