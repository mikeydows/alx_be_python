def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Perform division
        result = num / denom
        return f"Result: {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
