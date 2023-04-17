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