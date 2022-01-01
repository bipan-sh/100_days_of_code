import art
import game_data
import random
import os

print(art.logo)
def game():
    data = game_data.data
    game_over = False
    score = 0
    a_choser = random.randint(0, len(data)-1)
    b_choser = random.randint(0, len(data)-1)
    while a_choser == b_choser:
        a_choser = random.randint(0, len(data)-1)
        
    while not game_over:   
        a_choser = b_choser
        b_choser = random.randint(0, len(data)-1)
        while a_choser == b_choser:
            b_choser = random.randint(0, len(data)-1)
        print(f"Compare A: {data[a_choser]['name']}, a {data[a_choser]['description']}, from {data[a_choser]['country']}")
        print(art.vs)
        print(f"Against B: {data[b_choser]['name']}, a {data[b_choser]['description']}, from {data[b_choser]['country']}")
        answer = input('Choose A or B: ')


        if answer == 'A':
            if data[a_choser]['follower_count'] > data[b_choser]['follower_count']:
                print("That's correct")
                score += 1
            elif data[a_choser]['follower_count'] < data[b_choser]['follower_count']:
                print("That's incorrect")
                game_over = True

        elif answer == 'B':
            if data[a_choser]['follower_count'] > data[b_choser]['follower_count']:
                print("That's incorrect")
                
                game_over = True
            elif data[a_choser]['follower_count'] < data[b_choser]['follower_count']:
                print("That's correct")
                score += 1
        
        else:
            print('Wrong variable! Be careful next time')
            game_over = True

        os.system('cls')
        print(f"Score {score}")

    print('Game Over')
    print(f'Final score {score}')
 
while input('Do you want to play a game of higher or lower? Y or N ') == 'Y':
    game()

