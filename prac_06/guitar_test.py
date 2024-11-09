"""
Test code for Guitar class in guitar.py
"""

from guitar import Guitar

# Test code for Guitar class
test_guitar = Guitar('Gibson SG', 1952, 4000)
print(test_guitar)
print("Expected 72. Got: ", test_guitar.get_age())  # Default year is 2024
print("Expected True. Got: ", test_guitar.is_vintage())
