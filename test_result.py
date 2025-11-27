# Test script for result_card_generator.py with automated input
import io
import sys

# Simulate user input for 5 students with 5 subjects each
test_input = """Rahul Kumar
85
90
78
88
92
Priya Sharma
95
92
98
90
94
Amit Patel
72
68
75
70
73
Sneha Gupta
88
85
90
87
89
Vikram Singh
55
60
58
62
59
DONE
"""

sys.stdin = io.StringIO(test_input)

# Run the result card generator code
exec(open('F:\\python_code\\result_card_generator.py').read())
