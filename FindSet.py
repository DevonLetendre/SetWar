from setdeck import SetDeck

def atr_all(i,j,k,clist):
    # Checks if three cards are a set.
    for h in range(len(clist[0])):
        if (clist[i][h] == clist[j][h] == clist[k][h]):
            continue 
        elif (clist[i][h] != clist[j][h]) and (clist[i][h] != clist[k][h]) and (clist[j][h] != clist[k][h]):
            continue
        else:
            return False
    return True

def matcher(set_deck):
    '''
    Checks if there is a match among 3 or more cards. 
    Returns -1 if there is no match.
    Returns the position of the card that completes a match, if there is one. 
    '''
    blank = {}
    clist = []
    
    # Takes all elements out of the table deck object and puts them in a list.
    for h in range(len(set_deck)):
        temp = set_deck.popTopCard()
        if type(temp) == str or type(temp) == int:
            clist.append(temp) 
    
    # IMPORTANT - This puts the cards back into the setDeck object. 
    repair = [x for x in clist]
    for n in repair:
       set_deck.pushCardBottom(n)

    # Iterate over every trio combination of cards.
    for i in range(len(clist)):
        for j in range(1, len(clist)):
            for k in range(2, len(clist)):
                # If any of the cards are equal, skip over them since every card in the deck is unique.
                if (i == j) or (i == k) or (j == k):
                    continue
                elif atr_all(i,j,k,clist):
                    top = max(i,j,k)
                    blank[top] = [i,j,k]
    if len(blank) == 0:
        return -1
    else: 
        f = (min(blank))
        return max(blank[f]) + 1




