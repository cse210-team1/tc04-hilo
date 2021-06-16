#!/usr/bin/env python3
#from colorama import Fore, Style
import random
SPADE = 0
DIMOND = 1
HEART = 2
CLUB = 3

suits_symbols = ['♠', '♦', '♥', '♣']
card_values = {
	'Ace': 14,  # value of the ace is high until it needs to be low
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'10': 10,
	'Jack': 11,
	'Queen': 12,
	'King': 13
}


class Cards:
	""" This class contains all the behaviors needed for cards play.  
	This doesn't include actual game play, but rather the suffling and printing of the cards.
	This class is currently in development
	"""
	
	def __init__(self):
		""" Constructor Method.  initializes with an ordered deck of cards"""
		
		# TODO: IDEA: Maybe a card can be it's own class (more like struct) that holds the data
		# of the card it's self.  I think if things are done this way it will be easier to deal
		# and shuffle without needing to delete cards.
		
		self.new_deck()
		
	def create_card(self,rank,suit):
		lines = []
		space = " "
		suit = suits_symbols[suit]
		if rank == 10:
			space = ""
		elif rank == 11:
			rank = "J"
			space = " "
		elif rank == 12:
			rank = "Q"
			space = " "
		elif rank == 13:
			rank = "K"
			space = " "
		elif rank == 14:
			rank = "A"
		else:
			rank = rank
			
			
		lines.append(f'┌─────────┐')
		lines.append(f'│{rank}{space}       │')  # use two {} one for char, one for suit or char
		lines.append(f'│         │')
		lines.append(f'│         │')
		lines.append(f'│    {suit}    │')
		lines.append(f'│         │')
		lines.append(f'│         │')
		lines.append(f'│       {space}{rank}│')
		lines.append(f'└─────────┘')
		
		
#		if suit == '♦' or suit == '♥':
#			color = Fore.LIGHTRED_EX
#		else:
#			color = Fore.WHITE
		color = ""  # Color removed to decrease complexity
			

		card = []
		for line in lines:
			card.append(color + line)
		return card 
		
	def new_deck(self):
		""" Creates a new deck"""
		# This essetially unsuffles the deck, if eveything else works this shouldn't be needed
		
		deck = []
		for i in range(4):
			for j in range(2,15):
				deck.append(self.create_card(j,i))
		# This is one of the class atributes, and probably shouldn't be hiddent like this
		self.deck = deck
	
#	def shuffle(self):
#		""" Randomizes the initial deck"""
#		shuffled_deck = []
#		
#		while len(shuffled_deck) <= 51:
#			card = random.choice(self.deck)
#			if card in shuffled_deck:
#				pass
#			else:
#				shuffled_deck.append(card)
#			
#		self.deck = shuffled_deck
		
	def draw_card(self, Id):
		""" Selects and returns a card removing it from the deck"""
		
		Id = Id - 1
		split_card = self.deck[Id]
		card = ""
		for line in split_card:
			card += line + "\n"
		return card





	