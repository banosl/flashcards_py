class Deck: 
  def __init__(self, cards):
    self.cards = cards

  def count(self):
    return len(self.cards)

  def cards_in_category(self, category):
    by_category = []
    for card in self.cards:
      if (card.category == category):
        by_category.append(card) 
    return by_category