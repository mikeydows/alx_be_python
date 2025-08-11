# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Adds two numbers without using class or instance attributes."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Multiplies two numbers and prints the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Static method call
    sum_result = Calculator.add(7, 8)
    print(f"The sum is: {sum_result}")

    # Class method call
    product_result = Calculator.multiply(5, 10)
    print(f"The product is: {product_result}")
