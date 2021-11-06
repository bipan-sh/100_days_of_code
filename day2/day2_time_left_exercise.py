#count how much time you've left to live in days, weeks and months

age = input("What's your age? ")

years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {months_left} months, {weeks_left} weeks, and {days_left} days left to live")