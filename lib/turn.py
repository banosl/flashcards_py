class Turn:
  def __init__(self, guess, card):
    self.guess = guess
    self.card = card

  def check_correct(self):
    if self.guess == self.card.answer:
      return True
    else:
      return False
    
  def feedback(self):
    if self.check_correct() == True:
      return "Correct!"
    else:
      return "Incorrect!!!!!!! >:["