# ==============================================================================
# TOOL 2: GST Invoice Generator (console-based)
# Business Use-Case: Generates a clear, itemized invoice and applies the correct 
# GST rate to each product for tax compliance and final billing.
# Concepts Covered: Lists, while loop, for loop, if-elif, basic arithmetic.
# ==============================================================================

# Initialize parallel lists for storing item details 
item_names = []
quantities = []
rates = []
gst_percents = []

# --- Data Input Phase using a while loop ---
print("--- GST Invoice Item Entry ---")
print("Enter item details one by one. Type 'FINISH' when done.")

while True:
    # Ask customer to enter items one by one 
    item = input("\nEnter item name (or type 'FINISH'): ")
    
    # Check for the exit condition
    if item.upper() == 'FINISH':
        break
    
    item_names.append(item)
    
    # Input Quantity
    while True:
        try:
            qty = int(input(f"Enter quantity of '{item}': "))
            if qty <= 0:
                print("Quantity must be positive.")
                continue
            quantities.append(qty)
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")
            
    # Input Rate (Price per unit)
    while True:
        try:
            rate = float(input(f"Enter unit rate (Price before GST) of '{item}': "))
            if rate < 0:
                print("Rate cannot be negative.")
                continue
            rates.append(rate)
            break
        except ValueError:
            print("Invalid input. Please enter a number for the unit rate.")

    # Input GST Percentage (0, 5, 12, or 18)
    while True:
        try:
            gst_p = int(input(f"Enter GST percent for '{item}' (0, 5, 12, or 18): "))
            # Use if-elif to apply 0%, 5%, 12% or 18% GST 
            if gst_p in [0, 5, 12, 18]:
                gst_percents.append(gst_p)
                break
            else:
                print("Invalid GST percent. Please enter 0, 5, 12, or 18.")
        except ValueError:
            print("Invalid input. Please enter a whole number for GST percent.")


# --- Calculation and Output Phase using a for loop ---
total_bill_amount = 0.0
total_gst_collected = 0.0

print("\n" + "="*70)
print("                           GST TAX INVOICE")
print("="*70)
print(f"{'Item':<20}{'Qty':<5}{'Rate':<10}{'Tax %':<8}{'Tax Amt':<12}{'Line Total':<15}")
print("-" * 70)

# The for loop iterates through the list indices 
for i in range(len(item_names)):
    # Calculate values for the current item
    taxable_value = rates[i] * quantities[i]
    gst_rate = gst_percents[i] / 100.0
    gst_amount = taxable_value * gst_rate
    line_total = taxable_value + gst_amount
    
    # Accumulate totals
    total_bill_amount += taxable_value
    total_gst_collected += gst_amount
    
    # Print a neat invoice line
    print(f"{item_names[i]:<20}{quantities[i]:<5}${rates[i]:<9.2f}{gst_percents[i]:<7}%${gst_amount:<11.2f}${line_total:<14.2f}")

print("-" * 70)
# Print final invoice with grand total 
grand_total = total_bill_amount + total_gst_collected
print(f"{'Total Taxable Value:':<55}${total_bill_amount:<14.2f}")
print(f"{'Total GST Collected:':<55}${total_gst_collected:<14.2f}")
print("="*70)
print(f"{'GRAND TOTAL PAYABLE:':<55}${grand_total:<14.2f}")
print("="*70)