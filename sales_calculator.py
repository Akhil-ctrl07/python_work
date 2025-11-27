# ==============================================================================
# TOOL 1: Daily Sales & Profit Calculator for General Store
# Business Use-Case: Automates daily sales tracking, profit calculation, 
# and bill generation.
# Concepts Covered: Lists, while loop, for loop, basic arithmetic.
# ==============================================================================

# Initialize empty lists to store transaction data (parallel lists) 
item_names = []
quantities = []
cost_prices = [] # Cost to the store (for profit calculation)
selling_prices = [] # Price sold to the customer

# --- Data Input Phase using a while loop ---
print("--- Daily Sales Entry ---")
print("Enter sales transactions one by one. Type 'DONE' when finished.")

while True:
    # Get user input for the item name
    item = input("\nEnter item name (or type 'DONE'): ")
    
    # Check for the exit condition
    if item.upper() == 'DONE':
        break

    # Meaningful variable names are important [cite: 8]
    item_names.append(item)
    
    # Use input() to capture quantity, cost price, and selling price
    # The 'try-except' block is a good practice, but for core concept demonstration,
    # we'll use basic input and assume valid numerical entry.
    
    # Input for quantity sold
    while True:
        try:
            qty = int(input(f"Enter quantity of '{item}': "))
            if qty <= 0:
                print("Quantity must be a positive number.")
                continue
            quantities.append(qty)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")
            
    # Input for cost price
    while True:
        try:
            c_price = float(input(f"Enter cost price (CP) of '{item}' (per unit): "))
            if c_price < 0:
                print("Price cannot be negative.")
                continue
            cost_prices.append(c_price)
            break
        except ValueError:
            print("Invalid input. Please enter a number for cost price.")
            
    # Input for selling price
    while True:
        try:
            s_price = float(input(f"Enter selling price (SP) of '{item}' (per unit): "))
            if s_price < 0:
                print("Price cannot be negative.")
                continue
            if s_price < c_price:
                 print("Warning: Selling price is less than cost price (loss).")
            selling_prices.append(s_price)
            break
        except ValueError:
            print("Invalid input. Please enter a number for selling price.")
            
# --- Calculation and Output Phase using a for loop ---
total_sales = 0.0
total_profit = 0.0

print("\n" + "="*50)
print("              DAILY SALES REPORT & BILL")
print("="*50)
print(f"{'Item':<20}{'Qty':<5}{'SP/Unit':<10}{'Total Price':<15}")
print("-" * 50)

# The for loop iterates through the list indices 
for i in range(len(item_names)):
    # Calculate revenue for the item
    item_revenue = selling_prices[i] * quantities[i]
    
    # Calculate profit for the item
    item_profit = (selling_prices[i] - cost_prices[i]) * quantities[i]
    
    # Accumulate totals
    total_sales += item_revenue
    total_profit += item_profit
    
    # Print a neat bill line 
    print(f"{item_names[i]:<20}{quantities[i]:<5}${selling_prices[i]:<9.2f}${item_revenue:<14.2f}")

print("-" * 50)
# Print total sales and total profit 
print(f"{'TOTAL SALES REVENUE:':<40}${total_sales:<9.2f}")
print(f"{'TOTAL PROFIT:':<40}${total_profit:<9.2f}")
print("="*50)