from deckofcards import DeckOfCards
'''
A subclass of DeckOfCards. 
The set deck is a specific type of a deck of cards. 
'''
class SetDeck(DeckOfCards):
	def __init__(self, cards = None,pnum =None):
		DeckOfCards.__init__(self, cards)
		self.pnum = pnum
		
	def popTopCard(self):
		# Used by players to lay their card on table.
		return self.dealTop()

	def receiveDeck(self, deck):
		# Gives table deck to player if they win.
		self.addPileBottom(deck) 

	def pushCardBottom(self, card):
		# Adds player card to the table.
		self.addBottom(card)

	def setDeal(self, nplayers):
		# Deals cards to some number of players.
		PlayerRoster = []
		for player in (range(nplayers)):
			PlayerRoster.append(SetDeck(None,player))
		
		while len(self) != 0:
			for player in (range(nplayers)):
				PlayerRoster[player].addTop(self.dealTop())
				if len(self) == 0:
					return PlayerRoster
