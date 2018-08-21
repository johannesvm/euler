from random import shuffle

cards = []
suits = ['C', 'D', 'H', 'S']
for suit in suits:
    for i in range(1, 14):
        card = (i, suit)
        cards.append(card)
shuffle(cards)

draw = cards[:13]
sort = []
for suit in suits:
    for card in draw:
        if card[1] == suit:
            sort.append(card)

for i in range(0, 12):
    for j in range(0, i+1):
        if sort[i-j][1] == sort[i-j+1][1]:
            if sort[i-j][0] > sort[i-j+1][0]:
                temp = sort[i-j]
                sort[i-j] = sort[i-j+1]
                sort[i-j+1] = temp
            else:
                break;

print(sort)
        
