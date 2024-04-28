import random as rdm
import signal
import time

def get_secret_password(arrayLength):

    temp = []
    for i in range(arrayLength):

        temp.append(rdm.randint(0, 9))
        while(temp.count(temp[i]) > 1):
            temp.pop(i)
            temp.append(rdm.randint(0, 9))
    return temp

def validate_answer(secret, record, end_game, tentative):
    correct_numbers = 0
    correct_positions = 0
    tentative = list(map(lambda x: int(x), list(tentative)))

    for i in range (len(secret)):
        if (secret[i] == tentative[i]):
            correct_positions = correct_positions + 1
        if (secret.count(tentative[i]) == 1):
            correct_numbers = correct_numbers + 1
    
    if correct_numbers == 4 and correct_positions == 4:
        end_game = True
    else:
        end_game = False
    
    record = record + '\n' + str(tentative) + ' | ' + str(correct_numbers)+ ' | ' + str(correct_positions)
    return end_game, record
    # for i in range(secret.length):
    #     if (secret[i] == True):
    #         print(i)

