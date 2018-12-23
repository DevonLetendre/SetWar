# A superclass for a general set of cards
from mydatastructures import ListNode
from mydatastructures import DoublyLinkedList

class DeckOfCards:
	'''
	Takes either a string with cards separated by spaces, 
	or a list of strings, where each is a card.
	'''
	def __init__(self, L = None):
		self._L = DoublyLinkedList()
		if L != None:
			if (type(L) != str) and (type(L) != list):
				raise TypeError
			if type(L) == str:
				L = L.split()
			for item in L:
				self._L.addlast(item)

	def dealTop(self):
		# Removes and returns the card at the top of the deck.
		return self._L.removefirst()
	
	def dealBottom(self):
		# Removes and returns the card at the bottom of the deck.
		return self._L.removelast()
	
	def addTop(self, card):
		# Adds card to the top of the deck.
		self._L.addfirst(card)
	
	def addBottom(self, card):
		# Adds card to the bottom of the deck.
		self._L.addlast(card)
	
	def addPileTop(self, pile):
		'''
		Adds pile to the top of the deck. The pile should itself 
		be a deck of cards. After this operation, the bottom card 
		of pile will be on top of the (formerly) top card of the deck.
		'''
		pile._L += self._L
		self._L = pile._L
		pile._L = DoublyLinkedList()
		
	def addPileBottom(self, pile):
		'''
		Adds pile to the bottom of the deck. The pile should itself be 
		a deck of cards. After this operation, the top card of pile will 
		be below the (formerly) bottom card of the deck.
		'''
		self._L += pile._L 
	
	def deal(self, nplayers, ncards = None):
		'''
		Deals out ncards cards to nplayers players. 
		Returns a list or a tuple of decks corresponding to the hands of the different players. 
		Dealing is assumed to follow the standard conventions that one card is given at a time, 
		and each new card given is added to the top of the hand that receives it.
		'''
		PlayerRoster = []
		for player in (range(nplayers)):
			PlayerRoster.append(DeckOfCards())
		if ncards == None:
			while len(self._L) != 0:
				for player in (range(nplayers)):
					PlayerRoster[player].addTop(self._L.removefirst())
					if len(self._L) == 0:
						return PlayerRoster
		else:
			while len(ncards) != 0:
				for player in (range(nplayers)):
					PlayerRoster[player].addTop(self._L.removelast())
					ncards -= 1
					if len(ncards) == 0:
						return PlayerRoster

	def __len__(self):
		return len(self._L)









