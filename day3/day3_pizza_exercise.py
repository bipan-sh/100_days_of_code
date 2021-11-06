size = input('Which size pizza do you want? S M or L: ')

if size == 'S' :
    bill = 15
    peppa = input('Do you want to add pepperoni? Y or N. ')
    if peppa == 'Y':
        pepperoni = 2
    else :
        pepperoni = 0
    

elif size == 'M' :
    bill = 20
    peppa = input('Do you want to add pepperoni? Y or N. ')
    if peppa == 'Y':
        pepperoni = 3
    else :
        pepperoni = 0
    


elif size == 'L' :
    bill = 25
    peppa = input('Do you want to add pepperoni? Y or N. ')
    if peppa == 'Y':
        pepperoni = 3
    else :
        pepperoni = 0

want_cheese = input('Do you want to add cheese? Y or N ')

if want_cheese == 'Y':
    cheese = 2

else :
    want_cheese = 0 

total_bill = bill + pepperoni + cheese
print(f"Total bill is {total_bill}")
    


