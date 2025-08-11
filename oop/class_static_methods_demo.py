class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Only print the expected lines
print(f"The sum is: {Calculator.add(7, 8)}")
print(f"The product is: {Calculator.multiply(5, 10)}")
