class Calculator:
    calculation_type = "Arithmetic Operations"  # fixed spelling

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
print("Addition:", Calculator.add(3, 4))       # static method
print("Multiplication:", Calculator.multiply(5, 6))  # class method
