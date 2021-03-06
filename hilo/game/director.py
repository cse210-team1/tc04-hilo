from game.dealer import Dealer
from game.cards import Cards


class Director:
    def __init__(self):
        self.dealer = Dealer()
        self.guess = ""
        self.unicode_deck = Cards()

    def game_run(self):
        while self.can_play():
            self.get_inputs()
            self.do_outputs()
            if not self.can_play():
                print("Better luck next time!")
            elif input("Play again? [y/n] ") != "y":
                break
            print()
    def get_inputs(self):
        """ Gets a cards from the dealer, prints the card, and asks the user for a guess"""

        card = self.dealer.draw_card() - 1
        print("The card is: ")
        print(self.unicode_deck.draw_card(card))
        self.guess = input("Higher or Lower? [h/l] ")
        next_card = self.dealer.draw_card() - 1
        print(f"The next card is: ")
        print(self.unicode_deck.draw_card(next_card))
        

    def do_outputs(self):
        """ Gets the socre from the dealer and prints it"""
        score = self.dealer.calculate_points(self.guess)
        # If their score is 0 or below, end the game
        print(f"Your Score is: {score}")

    def can_play(self):
        if self.dealer.score <= 0:
            return False
        else:
            return True