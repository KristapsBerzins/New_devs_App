#!/usr/bin/env python3

print("Float Precision Loss (Finance Team)")
print("-------------------------")
amount = "333.333"
print(f'float("{amount}")         = {float(amount):.15f}')
print(f'round(float("{amount}"),2) = {round(float(amount), 2)}')
