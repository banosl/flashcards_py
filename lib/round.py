from lib.card import Card
from lib.deck import Deck
from lib.turn import Turn

class Round:
  def __init__(self, deck):
    self.deck = deck
    self.turns = []

  def current_card(self):
    return self.deck.cards[0]

  def take_turn(self, guess):
    new_turn = Turn(guess, self.current_card())
    self.turns.append(new_turn)
    self.deck.cards.pop(0)
    return new_turn

  def turn_correct(self, turn):
    return turn.check_correct()
  
  def number_correct(self):
    correct = []
    for turn in self.turns:
      if (turn.feedback() == "Correct!"):
        correct.append(turn)
    return len(correct)
  
  def number_correct_by_category(self, cat):
    cat_array = []
    correct = []
    for turn in self.turns:
      if (turn.card.category == cat):
        cat_array.append(turn)
    for turn in cat_array:
      if (turn.feedback() == "Correct!"):
        correct.append(turn)
    return len(correct)

  def percent_correct(self):
    total = len(self.turns)
    return round((self.number_correct()/total), 4) * 100
  
  def percent_correct_by_category(self, cat):
    cat_array = []
    correct_count = self.number_correct_by_category(cat)

    for turn in self.turns:
      if (turn.card.category == cat):
        cat_array.append(turn)

    return round((correct_count/len(cat_array)), 4) * 100
    
  