# The purpose of this program is to retrieve a user input and pass that input into a function and
# calculate a cost based on input and print receipt.

def calc_function(length, cost):
    total = feet * price
    return total


separator = '---------------------------'
company_name = input('Hello, Welcome to Fiber Installers. May I have your company name?')
feet = float(input('How many feet of Fiber Optic cable do you need?'))

if feet <= 100.0:
    price = 0.87
elif 100.1 <= feet < 250.0:
    price = 0.80
elif 250.1 <= feet < 500.0:
    price = 0.70
else:
    price = 0.50

calc_cost = '${:,.2f}'.format(calc_function(feet, price))

# Print receipt including Company name, Length of cable (in feet), Calculated cost, and Total cost.
# Separator added to break up input lines from output.

print(separator)
print('Receipt for Fiber Optic Cable')
print('Customer:' + company_name)
print('Requested Length (in feet): ' + str(feet))
print('Cost (per foot): $' + str(price).format('${:,.2f}'))
print('Total cost: ' + str(calc_cost))
print(separator)

