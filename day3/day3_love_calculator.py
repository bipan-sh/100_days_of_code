#Love calculator

#input your name and your gf's name
your_name = input('What is your name? ')
your_bae_name = input("Your bae's name? ")

#make them lower case
your_name = your_name.lower()
your_bae_name = your_bae_name.lower()

name = your_name + your_bae_name


#count the number of true love in the name
true_counter = int(name.count('t')) + int(name.count('r')) + int(name.count('u')) + int(name.count('e'))
love_counter = int(name.count('l')) + int(name.count('o')) + int(name.count('v')) + int(name.count('e'))

#converting the integer into string to add them
love_percentage = (str(true_counter) + str(love_counter))
love_percentage = int(love_percentage)

#conditions to say what happens on certain percentage 
if love_percentage < 10 or love_percentage > 90 :
    print(f"Your love percentage is {love_percentage}, break up!")

elif love_percentage > 40 or love_percentage < 50:
    print(f"Your love percentage is {love_percentage}, you're cute")

else :
    print(f"Your love score is {love_percentage}")
