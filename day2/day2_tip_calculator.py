#tip calculator

print("Welcome to the tip calculator")

total_bill = float(input('What was the total bill? $'))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

if tip == 10 or tip == 12 or tip == 15:
    each_pay = (total_bill + ((tip/100) * total_bill) ) / people
    print(f'Each person should pay: ${each_pay}')

else :
    print("invalid tipping amount")