from game.dealer import Dealer


class Director:
    def __init__(self):
        self.dealer = Dealer()
        self.guess = ""
        self.score = 300

    def game_run(self):
        while self.can_play():
            self.get_inputs()
            self.do_outputs()
            if input("Play again? [y/n] ") != "y":
                break
            print()
    def get_inputs(self):
        """ Gets a cards from the dealer, prints the card, and asks the user for a guess"""

        card = self.dealer.draw_card()
        print(f"The card is: {card}")
        self.guess = input("Higher or Lower? [h/l] ")
        next_card = self.dealer.draw_card()
        print(f"The next card is: {next_card}")

    def do_outputs(self):
        """ Gets the socre from the dealer and prints it"""
        self.score += self.dealer.calculate_points(self.guess)
        # If their score is 0 or below, end the game
        print(f"Your Score is: {self.score}")

    def can_play(self):
        if self.score <= 0:
            return False
        else:
            return True
