# Test script for sales_calculator.py with automated input
import io
import sys

# Simulate user input
test_input = """Laptop
2
800
1000
Mouse
5
10
15
Keyboard
3
25
40
DONE
"""

sys.stdin = io.StringIO(test_input)

# Run the sales calculator code
exec(open('F:\\python_code\\sales_calculator.py').read())
