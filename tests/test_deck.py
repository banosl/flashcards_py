from lib.card import Card
from lib.turn import Turn
from lib.deck import Deck

def test_deck():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
               "Mars",
              "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
              "North north west",
              "STEM")
  cards = [card1, card2, card3]
  deck = Deck(cards)

  assert deck.cards == cards
  assert deck.cards[1] == card2

def test_count():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
              "Mars",
              "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
              "North north west",
              "STEM")
  cards = [card1, card2, card3]
  deck = Deck(cards)

  result = deck.count()
  assert result == 3
   
  result = deck.count()
  assert result != 4

def test_cards_in_category():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
              "Mars",
              "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
              "North north west",
              "STEM")
  cards = [card1, card2, card3]
  deck = Deck(cards)

  result = deck.cards_in_category("Geography")
  assert result == [card1]
  
  result = deck.cards_in_category("STEM")
  assert result == [card2, card3]

  result = deck.cards_in_category("Pop")
  assert result == []