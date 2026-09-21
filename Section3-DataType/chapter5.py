import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49999999

diff_temp = ideal_temp - current_temp

print(f"Temperature difference : {diff_temp}")