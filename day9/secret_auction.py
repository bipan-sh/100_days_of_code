import os 
import art

print(art.gavel)

end_of_bid = False
bidders = {}
while end_of_bid is False:


    name = input("What is your name? \n")
    bid = int(input("How much do you bid? \n"))
    bidders[name] = bid

    bid_continue = input("Is there any other bidder? Press y for yes or n for no\n"). lower()
    os.system('cls')
    if bid_continue == 'n':
        end_of_bid = True


def finding_highest() :
    highest_value = 0
    winner = ""

    for name in bidders:
        if bidders[name] > highest_value:
            highest_value = bidders[name]
            winner = name

    print(f"The highest bidder is {winner} with {highest_value}")

finding_highest()