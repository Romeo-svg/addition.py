def calculate_commission(sales):
    if sales >= 100000:
        rate = 10
        remark = "Excellent Sales"
    elif sales >= 50000:
        rate = 7
        remark = "Good Sales"
    else:
        rate = 5
        remark = "Needs Improvement"

    commission = sales * rate / 100
    return commission, rate, remark


# Input from user
sales_amount = float(input("Enter sales amount (KES): "))

# Function call
commission, rate, remark = calculate_commission(sales_amount)

# Output
print("\nSales Amount: KES", sales_amount)
print("Commission Rate:", rate, "%")
print("Commission Earned: KES", commission)
print("Remark:", remark)
