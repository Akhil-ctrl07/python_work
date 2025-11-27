# Test script for discount_calculator.py with automated input
import io
import sys

# Simulate user input
test_input = """Shirt
2
500
Jeans
1
1200
Shoes
1
1500
BILL
"""

sys.stdin = io.StringIO(test_input)

# Run the discount calculator code
exec(open('F:\\python_code\\discount_calculator.py').read())
