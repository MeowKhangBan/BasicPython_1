import random
def play(player = None):
    try:
        bot = ['r','p','s']
        bot_answer = random.choice(bot)
        if player == bot_answer:
            return 'Draw \nPlayer : Rock \nBot : Rock'
        elif player == 'r' and bot_answer  == 's':
            return 'You win \nPlayer : Rock \nBot : Paper'
        elif player == 'p' and bot_answer  == 'r':
            return 'You win \nPlayer : Paper \nBot : Rock'
        elif player == 's' and bot_answer  == 'p':
            return 'You win \nPlayer : Scissors \nBot : Paper'
        else:
            return 'You lose Noob'
    except:
        return 'Error 001'

while True :
    player = str(input('[r]ock , [p]aper , [s]cissors, E[x]it :'))
    if player == 'x':
        print('---------------------')
        print('Why are you running ???')
        print('---------------------')
        break
    else:
        print('---------------------')
        print(play(player))
        print('---------------------')
        break
