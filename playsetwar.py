#Main Module
#INPUT: Number of players and a string of cards
#OUTPUT: A string that says which player won and how many rounds it took
from setdeck import SetDeck
from FindSet import matcher
import sys 

#A function that can play setWar if given the number of players and a list of cards
def play(playerDecks,tableDeck):
	rounds = 0
	winnerNum = 0
	winnerBool = False
	matchBool = False
	index = 0

	while not winnerBool:
		while not matchBool:
			
			tableDeck.pushCardBottom(playerDecks[index].popTopCard())

			if len(tableDeck) >= 3:
				if matcher(tableDeck) != -1:
					playerDecks[index].receiveDeck(tableDeck)
					playerDecks = playerDecks[index : ] + playerDecks[ : index] 
					rounds = rounds + 1
					index  = 0 
					break

			if (len(playerDecks[index]) == 0):
					del playerDecks[index]
					index = index - 1
					if (len(playerDecks)) == 0:
						winnerBool = True
						rounds = 1
						break

			if playerDecks[index] == playerDecks[-1]:
				index = 0
				continue

			index = index + 1

		if len(playerDecks) == 1:
			winnerNum = playerDecks
			winnerBool = True

	if len(playerDecks) == 0:
		winnerNum = 0
	else:
		winnerNum = winnerNum[0].pnum

	if rounds == 1:
		print("Player %d won in %d round." % (winnerNum, rounds))
	else:
		print("Player %d won in %d rounds." % (winnerNum, rounds))

#Takes input if called externally
if __name__ == "__main__":
	cards = []
	players = 0
	for line in sys.stdin:
		for n in line.split():
			if players == 0:
				players = int(n)
				continue
			cards.append(n)
	myDeck = SetDeck(cards)
	playerDecks = myDeck.setDeal(players)
	tableDeck = SetDeck()
	play(playerDecks, tableDeck)

