# DSC510
# Week 3
# Fiber Optic cable cost program
# Author Chris Nosky
# 09/14/20
# The purpose of this program is to retrieve a user input and calculate a cost based on input and print receipt.
separator = '---------------------------'

# Display welcome message and user input request.
company_name = input('Hello, Welcome to Fiber Installers. May I have your company name?')

# Request number of feet of fiber optic cable to be installed from user.
length_needed = input('How many feet of Fiber optic cable do you need installed?')

# Calculate installation cost of fiber optic cable based on length.
cable_cost = 0.0


if float(length_needed) <= 100.0:
    cable_cost = 0.87
elif 100.1 <= float(length_needed) < 250.0:
    cable_cost = 0.80
elif 250.1 <= float(length_needed) < 500.0:
    cable_cost = 0.70
else:
    cable_cost = 0.50


cost_calc = 0.00

if float(length_needed) <= 100:
    cost_calc = float(length_needed) * 0.87
elif 100.1 <= float(length_needed) < 250:
    cost_calc = float(length_needed) * 0.80
elif 250.1 <= float(length_needed) < 500:
    cost_calc = float(length_needed) * 0.70
else:
    cost_calc = float(length_needed) * 0.50

# Print receipt including Company name, Length of cable (in feet), Calculated cost, and Total cost.
# Separator added to break up input lines from output.
print(separator)
print('Receipt for Fiber Optic Cable')
print('Customer:' + company_name)
print('Requested Length (in feet): ' + length_needed)
print('Cost (per foot): $' + str(cable_cost))
print('Total cost: $' + str(cost_calc))
print(separator)



def calc(cost):
    if float(length_needed) <= 100:
        cost_calc = float(length_needed) * 0.87
    elif 100.1 <= float(length_needed) < 250:
        cost_calc = float(length_needed) * 0.80
    elif 250.1 <= float(length_needed) < 500:
        cost_calc = float(length_needed) * 0.70
    else:
        cost_calc = float(length_needed) * 0.50
    return str(cost_calc)
