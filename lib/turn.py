class Turn:
  def __init__(self, guess, card):
    self.guess = guess
    self.card = card

  def correct(self):
    if self.guess == self.card.answer:
      return True
    else:
      return False