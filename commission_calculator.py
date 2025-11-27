# ==============================================================================
# TOOL 6: Sales Commission Calculator with Multiple Slabs
# Business Use-Case: Calculates salesperson commission based on tiered sales slabs,
# automating payroll and ensuring correct bonus payouts.
# Concepts Covered: Lists, for loop, nested if-elif-else.
# ==============================================================================

# Initialize parallel lists
salespersons = []
sales_amounts = []

# --- Data Input Phase using a simple loop (5-8 salespeople required) ---
print("--- Sales Commission Data Entry ---")
print("Enter data for 5 to 8 salespeople.")

for i in range(8): # Loop up to 8 times to allow for minimum 5
    # Input Name
    name = input(f"\nEnter name of Salesperson #{i + 1} (or type 'DONE' if 5+ names entered): ")
    
    if name.upper() == 'DONE':
        if len(salespersons) < 5:
            print("You must enter data for at least 5 salespeople.")
            continue
        else:
            break
            
    salespersons.append(name)
    
    # Input Sales Amount
    while True:
        try:
            sales = float(input(f"Enter total sales amount (in ₹) for {name}: "))
            if sales < 0:
                print("Sales amount cannot be negative.")
                continue
            sales_amounts.append(sales)
            break
        except ValueError:
            print("Invalid input. Please enter a number for sales.")

# --- Calculation and Output Phase using a for loop ---
print("\n" + "="*70)
print("                  SALES COMMISSION SLIP")
print("="*70)
print(f"{'Salesperson':<20}{'Sales (₹)':<15}{'Commission %':<15}{'Commission (₹)':<15}{'Bonus':<5}")
print("-" * 70)

# The for loop iterates through the list indices
for i in range(len(salespersons)):
    sales = sales_amounts[i]
    commission_rate = 0.0
    commission_amount = 0.0
    bonus = 0
    
    # Use if-elif-else inside a for loop to determine commission slab and bonus
    if sales <= 40000:
        commission_rate = 0.05  # 5%
    elif sales <= 80000:
        commission_rate = 0.08  # 8%
    elif sales <= 120000:
        commission_rate = 0.10 # 10%
    elif sales > 120000:
        commission_rate = 0.15 # 15%
        bonus = 2000           # + ₹2000 bonus

    # Calculate the commission amount
    commission_amount = sales * commission_rate
    
    # Calculate the final payout
    total_payout = commission_amount + bonus
    
    # Print commission slip line
    print(f"{salespersons[i]:<20}{sales:<15.2f}{commission_rate*100:<14.0f}%{total_payout:<14.2f}{'Yes' if bonus > 0 else 'No':<5}")

print("="*70)