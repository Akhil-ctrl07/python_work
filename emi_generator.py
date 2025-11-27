# ==============================================================================
# TOOL 9: EMI & Loan Repayment Schedule Generator
# Business Use-Case: Calculates the Equated Monthly Installment (EMI) and generates
# a detailed month-wise repayment schedule for a loan.
# Concepts Covered: Basic input/output, formula calculation, while loop, operators.
# ==============================================================================

import math # Required for the power function math.pow() or ** operator

print("--- EMI and Loan Repayment Schedule Generator ---")

# --- Input Phase ---
while True:
    try:
        # Take principal, rate, months using input()
        principal = float(input("Enter Principal Loan Amount (P) in ₹: "))
        if principal <= 0:
            print("Principal must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        annual_rate = float(input("Enter Annual Interest Rate (R) in % (e.g., 10.5): "))
        if annual_rate <= 0:
            print("Rate must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
        
while True:
    try:
        months = int(input("Enter Loan Tenure in Months (N): "))
        if months <= 0:
            print("Tenure must be a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# --- Calculation Phase ---
# Monthly Interest Rate (r) 
# Formula: r = (Annual Rate / 100) / 12
monthly_rate = (annual_rate / 100) / 12

# Calculate EMI using formula: 
# EMI = [ P * r * (1 + r)^N ] / [ (1 + r)^N – 1 ]
if monthly_rate == 0:
    # Handle zero interest rate case (simple division)
    emi = principal / months
else:
    # Formula components:
    power_factor = math.pow((1 + monthly_rate), months)
    emi = (principal * monthly_rate * power_factor) / (power_factor - 1)

# Initialize variables for the schedule
remaining_balance = principal
total_interest_paid = 0.0
total_principal_paid = 0.0

# --- Output Phase: Month-wise Schedule ---
print("\n" + "="*85)
print(f"LOAN SUMMARY: Principal=₹{principal:.2f}, Rate={annual_rate}%, Tenure={months} months")
print(f"Calculated EMI: **₹{emi:.2f}**")
print("="*85)
# Print table header
print(f"{'Month':<7}{'EMI':<12}{'Interest':<15}{'Principal':<15}{'Balance':<16}{'Total Interest':<15}")
print("-" * 85)

# Use while or for loop to print month-wise table
month_number = 1
while month_number <= months:
    # 1. Calculate Interest for the month
    interest_paid = remaining_balance * monthly_rate
    
    # 2. Calculate Principal component of EMI
    principal_paid = emi - interest_paid
    
    # Check to prevent negative balance at the last month due to rounding
    if month_number == months:
        principal_paid = remaining_balance # Pay off the exact remaining balance
        emi = remaining_balance + interest_paid # EMI slightly adjusted
    
    # 3. Calculate New Balance
    remaining_balance -= principal_paid
    
    # Accumulate totals (for summary)
    total_interest_paid += interest_paid
    total_principal_paid += principal_paid
    
    # Print month-wise table line
    print(f"{month_number:<7}{emi:<12.2f}{interest_paid:<15.2f}{principal_paid:<15.2f}{remaining_balance:<16.2f}{total_interest_paid:<15.2f}")
    
    month_number += 1

print("="*85)
print(f"SUMMARY: Total amount paid: ₹{(principal + total_interest_paid):.2f}")
print(f"SUMMARY: Total Interest Paid over term: **₹{total_interest_paid:.2f}**")
print("="*85)