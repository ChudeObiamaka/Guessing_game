print("Welcome to the Guess the Number game!")
print("I am thinking of a numberbetween 1 and 100. Can you guess what it is?")
secret_num = 75
guess = 0
guess_limit = 5 #Maximum number a user is going to guess
guess_number = 0 #Current guess number
guess = int(input(f'Guess a number 1-100: '))
guess_number += 1
while guess_number < guess_limit:
    if guess != secret_num:
        guess_number +=1
        if guess > secret_num:
            guess = int(input(f'{guess}Your guess is too high - Guess again 1-100: '))
    else:
        guess = int(input(f'{guess}Your guess is too low - Guess again 1-100: '))
        if guess == secret_num:
            print(f'Congratulations! You guessed the number correctly {guess}')
            break
        if guess != secret_num:
            print(f'Sorry you lose! it was {secret_num}')