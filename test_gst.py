# Test script for gst_invoice_generator.py with automated input
import io
import sys

# Simulate user input
test_input = """Rice
10
50
5
Oil
2
150
12
Electronics
1
5000
18
FINISH
"""

sys.stdin = io.StringIO(test_input)

# Run the GST invoice generator code
exec(open('F:\\python_code\\gst_invoice_generator.py').read())
