import random

def compare(guess, number):
    global game_over
    global life
    if life == 0:
        print('You lose')
        game_over = True
    if guess > number:
        print('Too high \nGuess again')
    if guess < number:
        print('Too low \nGuess again')
    if guess == number:
        print("You're correct! \nThanks for playing!")
        game_over = True

def game_mode(difficulty):
    global life
    if difficulty == 'easy':
        life = 10
    if difficulty == 'hard':
        life = 5

def game():
    global life
    global game_over
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 101)
    difficulty = input("Choose the difficulty. Type easy or hard: ")
    game_over = False

    game_mode(difficulty)
    while not game_over:
        print(f"You have {life} life remaining to guess the number")
        guess = int(input('Make a guess: '))
        compare(guess, number)
        life -= 1
        if life == 0:
            print('You lose!')
            game_over = True

while input('Do you want to play number guessing game. Type y for yes and n for no: ') != 'n':
    game() 