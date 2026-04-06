import random

COLORS = ['B', 'G', 'Y', 'O', 'R', 'W']
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code


def guess_code():

    while True:
        guess = input('Guess: ').upper().split(' ')
        print(guess)
        if len(guess) != CODE_LENGTH:
            print(f'You must guess {CODE_LENGTH} colours.')
            continue

        for color in guess:
            if color not in COLORS:
                print(f'Invalid color{color}. Try again.')
                break

        else:
            break

    return guess


def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    code = generate_code()
    print(code)
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        if correct_pos == CODE_LENGTH:
            print(f'You got it!! Attempts: {attempts}')
            break
        print(
            f'Correct Positions: {correct_pos} | Incorrect positions: {incorrect_pos}')

    else:
        print('You ran out of tries, the code was:', *code)


if __name__ == '__main__':
    game()
