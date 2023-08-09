#!/usr/bin/python3
combinations = ['{}{}'.format(a, z) for a in range(10) for z in range(10) if a < z]
print(', '.join(combinations))
