# Test script for emi_generator.py with automated input
import io
import sys

# Simulate user input: Principal=100000, Rate=10.5%, Tenure=12 months
test_input = """100000
10.5
12
"""

sys.stdin = io.StringIO(test_input)

# Run the EMI generator code
exec(open('F:\\python_code\\emi_generator.py').read())
