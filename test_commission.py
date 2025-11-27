# Test script for commission_calculator.py with automated input
import io
import sys

# Simulate user input for 5 salespeople
test_input = """Alice Johnson
50000
Bob Smith
90000
Carol White
120000
David Brown
150000
Eve Davis
35000
DONE
"""

sys.stdin = io.StringIO(test_input)

# Run the commission calculator code
exec(open('F:\\python_code\\commission_calculator.py').read())
