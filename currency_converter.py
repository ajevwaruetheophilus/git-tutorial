# Program converts dollars to naira
dollar_amount = float(input("Enter amount in dollar: "))
conversion_unit = 1600
naira_amount = dollar_amount * conversion_unit
print(f"${dollar_amount:.2f} dollars is equivalent to #{naira_amount:,.2f}") 
