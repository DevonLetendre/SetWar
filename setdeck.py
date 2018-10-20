#A subclass of DeckOfCards 

from deckofcards import DeckOfCards

class SetDeck(DeckOfCards):
	def __init__(self, cards = None,pnum =None):
		DeckOfCards.__init__(self, cards)
		self.pnum = pnum

	#Used by players to lay their card on table
	def popTopCard(self):
		return self.dealTop()

	#Gives table deck to player if they win
	def receiveDeck(self, deck):
		self.addPileBottom(deck) 

	#Adds player card to the table
	def pushCardBottom(self, card):
		self.addBottom(card)

	#Deals cards to some number of players
	def setDeal(self, nplayers):
		PlayerRoster = []
		for player in (range(nplayers)):
			PlayerRoster.append(SetDeck(None,player))
		
		while len(self) != 0:
			for player in (range(nplayers)):
				PlayerRoster[player].addTop(self.dealTop())
				if len(self) == 0:
					return PlayerRoster
		




