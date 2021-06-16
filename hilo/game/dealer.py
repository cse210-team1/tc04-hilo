import random

class Dealer:
    # Define the points and initialize the card
    def __init__(self):
        self.score = 300
        self.current_card = 0
        self.previous_card = 0
    # Generate a random card to draw and return
    def draw_card(self):
        self.previous_card = self.current_card
        self.current_card = random.randint(1, 14)
        return self.current_card
    # Take the user guess and calculate their points after gaining/losing
    def calculate_points(self, guess):
        # If statements for each scenario
        if guess == "h" and self.current_card >= self.previous_card:
            self.score += 100
        elif guess == "h" and self.current_card < self.previous_card:
            if self.score < 75:
                self.score = 0
            else:
                self.score -= 75
        elif guess == "l" and self.current_card >= self.previous_card:
            if self.score < 75:
                self.score = 0
            else:
                self.score -= 75
        elif guess == "l" and self.current_card < self.previous_card:
            self.score += 100
        # Return the score for the director to deal with
        return self.score
