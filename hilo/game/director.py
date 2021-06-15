from game.dealer import dealer

class Director:
    def __init__(self):
        
        self.dealer = dealer()
        
    def game_run(self):
        while can_play():
            
            get_inputs()
            do_outputs()
            if input("Play again? [y/n]") == "n":
                break
            

    def get_inputs(self):
        """ Gets a cards from the dealer, prints the card, and asks the user for a guess"""
        
        self.card = self.dealer.draw_card()
        print(f"The card is: {self.card}")
        self.guess = input("Higher or Lower? [h/l] ")

    def do_outputs(self):
        """ Gets the socre from the dealer and prints it"""
        self.score = self.dealer.calculate_points()
        print(f"Your Score is: {score}")
            
    def can_play():
        if self.score <= 0:
            return False
        else:
            return True
        