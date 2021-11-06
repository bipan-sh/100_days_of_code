#Bank Roulette exercise 
import random

names = input("Give me names of everyone who's playing Bank Roulette seperated by a comma ( , ): ")

#Splitting the input by comma and space and creating a list
names_list = names.split(", ")

#Used the below print statements to debug
# print(names_list)
# print(len(names_list))

#Generating a random number from 0 which is the first item in the list to the end as len function gives the total item in the list
# and subtracting it by 1 as list starts with a 0 
random_number = random.randint(0, len(names_list)-1)

print(f"{names_list[random_number]} is going to buy the meal today.")