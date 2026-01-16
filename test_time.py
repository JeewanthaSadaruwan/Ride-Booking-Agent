#!/usr/bin/env python3
"""Test script to verify get_current_datetime is working correctly."""

import sys
sys.path.insert(0, '.')
from tools.get_current_datetime import get_current_datetime
import time

print('Test 1:')
result1 = get_current_datetime()
print(f"Message: {result1['message']}")
print(f"Time: {result1['time']}")
print(f"Full datetime: {result1['current_datetime']}")

time.sleep(3)

print('\nTest 2 (after 3 seconds):')
result2 = get_current_datetime()
print(f"Message: {result2['message']}")
print(f"Time: {result2['time']}")
print(f"Full datetime: {result2['current_datetime']}")

print(f"\nTime difference: {result2['time']} vs {result1['time']}")
print(f"Are they different? {result1['time'] != result2['time']}")
