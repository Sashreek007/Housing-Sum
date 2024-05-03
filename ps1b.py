def calculate_months_to_save(annual_salary, portion_saved, total_cost,semi_annual_raise):
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary / 12
    down_payment = total_cost * portion_down_payment
    months = 0
    
    while current_savings < down_payment:
        current_savings += current_savings * r / 12 + monthly_salary * portion_saved
        months += 1
        if months%6==0:
            annual_salary*=(1+semi_annual_raise)
            monthly_salary= (annual_salary)/12
        
    return months

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter you annual salary raise:"))


months = calculate_months_to_save(annual_salary, portion_saved, total_cost,semi_annual_raise)

print("Number of months:", months)
