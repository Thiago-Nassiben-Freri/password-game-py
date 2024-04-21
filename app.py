import random
from time import sleep


def exit(): 
    print('Okay, leaving...')
    sleep(2)
    print('Program finished!')

def password_generator(password_answer):
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '1234567890'
    spc_char = '!@#$%&*'
    tamanho = random.randint(5, 15)

    all_chars = char + num + spc_char

    password = ''.join(random.choice(all_chars) for c in range(tamanho))
    
    if password_answer == password:
        return True, f'You hit! the answer is: {password}'
    else:
        return False, f'You missed! the answer is: {password}'

def password_game_UX():
    attempts = 3

    while attempts > 0:
        var_choice = str(input('Do you want to play Password Game [Y/N]: '))

        if var_choice.upper() == 'Y': 
            var_answer = str(input('Enter your password answer: '))

            correct, message = password_generator(var_answer)

            if correct:
                print(message)
                break
            else: 
                attempts -= 1
                print(message)
                print(f'Remaining attempts: {attempts}')

                if attempts == 0: 
                    print('Your attempts are over. Better luck next time!')
        elif var_choice.upper() == 'N': 
            exit()
            break

if __name__ == '__main__': 
    password_game_UX()
