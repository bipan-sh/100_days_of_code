import random

names = ['anmol', 'bipan', 'rishav', 'rashrav', 'sansar', 'sumeet']
club = ['RM', 'PSG', 'Liv', 'M City', 'M Utd', 'Bayern']

already_selected_name = []
already_selected_club = []



for name in names:
    print(f"The person's name is {name}")
    name_club = random.choice(club)
    if name_club not in already_selected_club:
        print(f"They've got {name_club}")
    already_selected_club.append(name_club)
#haven't changed anything
