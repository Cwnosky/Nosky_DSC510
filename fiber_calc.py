# DSC510
# Week 2
# Fiber Optic cable cost program
# Author Chris Nosky
# 09/06/20
# The purpose of this program is to retrieve a user input and calculate a cost based on input and print receipt.
separator = '---------------------------'

# Display welcome message and user input request.
company_name = input('Hello, Welcome to Fiber Installers. May I have your company name?')

# Request number of feet of fiber optic cable to be installed from user.
length_needed = input('How many feet of Fiber optic cable do you need installed?')

# Calculate installation cost of fiber optic cable 'length_needed * 0.87'.
cable_cost = 0.87
cost_calc = float(length_needed) * 0.87

# Print receipt including Company name, Length of cable (in feet), Calculated cost, and Total cost.
# Separator added to break up input lines from output.
print(separator)
print('Receipt for Fiber Optic Cable')
print('Customer:' + company_name)
print('Requested Length (in feet): ' + length_needed)
print('Cost (per foot): $' + str(cable_cost))
print('Total cost: $' + str(cost_calc))
print(separator)
