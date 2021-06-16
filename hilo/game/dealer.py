import random

class Dealer:
    # Define the points and initialize the card
    def __init__(self):
        self.points = 300
        self.current_card = 0
        self.previous_card = 0
    # Generate a random card to draw and return
    def draw_card(self):
        self.previous_card = self.current_card
        self.current_card = random.randint(1, 13)
        return self.current_card
    # Take the user guess and calculate their points after gaining/losing
    def calculate_points(self, guess):
        pass