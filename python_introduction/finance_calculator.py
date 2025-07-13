monthly_income = int(input("Enter your monthly income?"))
monthly_expenses = int(input("Enter your monthly expenses?"))

monthly_savings = monthly_income - monthly_expenses

principal = monthly_savings
rate = 0.05
monthly = 12 * monthly_savings
interest = principal * rate * monthly_savings

projected_savings = monthly + interest

print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_savings)