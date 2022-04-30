import random

suit = ['\u2660','\u2665','\u2666','\u2663']
character = list('A23456789') + ['10'] +list('JMK')
def playing_card():
    deck = []
    for suit_pic in suit:
        for k in character:
            deck.append(suit_pic+k)
    return deck

d = playing_card()
p = random.sample(d,3)
print(p)
