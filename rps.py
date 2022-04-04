#!/usr/env/bin python3
import random, sys, math

while True:
    print('Are you ready to play rock, paper, scissors?')
    print('Yes: Type (y); No: Type (n)')
    answer_boolean = input()
    if answer_boolean == 'y':
        break
    elif answer_boolean == 'n':
        sys(exit)



def getmove ():
    wins = 0
    losses = 0
    ties = 0

    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        #if player_move == 'r' or player_move == 'p' or player_move == 's':
        #print('Type one of r, p, s, or q.')


        if player_move == 'r':
            print('ROCK versus ...')
            computermove()
            break

        elif player_move == 'p':
            print('PAPER versus ...')
            computermove()
            break
        elif player_move == 's':
            print('SCISSOR versus ...')
            computermove()
            break


def computermove ():
    random_number = random.randint(1, 3)
    if random_number == '1':
        computer_move = 'r'
        print('ROCK')
        return computer_move

    elif random_number == '2':
        computer_move = 'p'
        print('PAPER')
        return computer_move
    elif random_number == '3':
        computer_move = 's'
        print('SCISSOR')
        return computer_move

def computerversusplayer(player_move, computer_move):
    if player_move == computer_move:
        rint('It is a tie!')
        ties = ties + 1

    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        win = win + 1

    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        win = win + 1

    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        win = win + 1


    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1

    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1

    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1

getmove()

