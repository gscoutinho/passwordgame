from lib import *
import random as rdm
import os
import time

print('WELCOME TO THE SECRET PASSWORD!')
print('YOU HAVE TO GUESS THE SECRET PASSWORD!')
print('IT IS MADE OF 4 RANDOM NUMBER FROM 0 TO 9, WITH NO DUPLICATED NUMBER')
print('prepare yourself...')

secret_password = (get_secret_password(4))
os.system('cls')

record = 'FIND THE SECRET PASSWORD!!'

record = record + '\n' + '_ _ _ _ | correct numbers | correct positions'
print(record)

end_game = False


while(end_game == False):

    guess = input('Guess the SECRET PASSWORD: ')
    end_game, record = validate_answer(secret_password, record, end_game, guess)
    os.system('cls')
    print(record)

print('CONGRATULATIONS!! YOU WON!!!!!')

