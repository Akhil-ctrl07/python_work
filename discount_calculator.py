# ==============================================================================
# TOOL 8: Festival/Offer Discount & Final Billing Calculator
# Business Use-Case: Automatically applies tiered discounts and adds promotional 
# messages based on the customer's total purchase value during a sale or festival.
# Concepts Covered: Lists, for loop, if-elif-else, input/output.
# ==============================================================================

# Initialize parallel lists for product details
products = []
prices = [] # Price per unit
qty = []

# --- Data Input Phase using a while loop ---
print("--- Festival Offer Billing Entry ---")
print("Enter item details one by one. Type 'BILL' to finalize the order.")

while True:
    product_name = input("\nEnter Product Name (or type 'BILL'): ")
    
    # Check for the exit condition
    if product_name.upper() == 'BILL':
        break
    
    products.append(product_name)
    
    # Input Price
    while True:
        try:
            unit_price = float(input(f"Enter unit price (₹) for '{product_name}': "))
            if unit_price <= 0:
                print("Price must be positive.")
                continue
            prices.append(unit_price)
            break
        except ValueError:
            print("Invalid input. Please enter a number for the price.")
            
    # Input Quantity
    while True:
        try:
            quantity = int(input(f"Enter quantity of '{product_name}': "))
            if quantity <= 0:
                print("Quantity must be a whole positive number.")
                continue
            qty.append(quantity)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")

# --- Calculation and Output Phase using a for loop ---
sub_total = 0.0

print("\n" + "="*50)
print("             OFFER INVOICE BREAKDOWN")
print("="*50)
print(f"{'Product':<25}{'Qty':<5}{'Rate':<10}{'Line Total (₹)':<10}")
print("-" * 50)

# Calculate the sub-total (total before discount)
for i in range(len(products)):
    line_total = prices[i] * qty[i]
    sub_total += line_total
    print(f"{products[i]:<25}{qty[i]:<5}{prices[i]:<9.2f}{line_total:<9.2f}")

print("-" * 50)
print(f"{'SUB-TOTAL (Before Discount):':<40}{sub_total:<9.2f}")

# --- Discount Logic using if-elif-else ---
discount_rate = 0.0
discount_message = "No special offer applied."
free_gift_message = ""

# Use if-elif-else inside for loop: Bill < ₹999 -> 10%, ₹1000-₹2999 -> 20%, >=₹3000 -> 30% + free gift message.
if sub_total < 999:
    discount_rate = 0.10 # 10%
    discount_message = "Applied 10% Festival Discount."
elif sub_total < 3000: # This covers ₹1000 to ₹2999
    discount_rate = 0.20 # 20%
    discount_message = "Applied 20% Mega Offer Discount!"
else: # sub_total >= 3000
    discount_rate = 0.30 # 30%
    discount_message = "Applied 30% VIP Discount!"
    free_gift_message = "**Congratulations! You qualify for a FREE gift!**"

discount_amount = sub_total * discount_rate
final_payable_amount = sub_total - discount_amount

# --- Final Output ---
print(f"{'Discount Applied (Rate):':<40}{discount_rate * 100:.0f}%")
print(f"{'Discount Amount:':<40}{discount_amount:<9.2f}")
print("-" * 50)
print(f"{'FINAL PAYABLE AMOUNT:':<40}**{final_payable_amount:<9.2f}**")
print("="*50)
print(free_gift_message)