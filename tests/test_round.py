from lib.card import Card
from lib.deck import Deck
from lib.turn import Turn
from lib.round import Round


def test_round():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
              "Mars",
              "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
              "North north west",
              "STEM")
  cards = [card1, card2, card3]

  deck = Deck(cards)
  
  round = Round(deck)

  assert round.deck == deck
  assert round.turns == []

def test_current_card():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
               "Mars",
               "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
               "North north west",
               "STEM")
  cards = [card1, card2, card3]

  deck = Deck(cards)

  round = Round(deck)

  result = round.current_card()
  assert result == card1

  result = round.current_card()
  assert result != card2

def test_take_turn():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
               "Mars",
               "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
               "North north west",
               "STEM")
  cards = [card1, card2, card3]

  deck = Deck(cards)

  round = Round(deck)

  round.take_turn("Juneau")
  result = round.turns[0]

  assert result.guess == "juneau"

  round.take_turn("Nashville")
  result = round.turns[1]

  assert result.guess == "nashville"

def test_turn_correct():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
               "Mars",
               "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
               "North north west",
               "STEM")
  cards = [card1, card2, card3]

  deck = Deck(cards)

  round = Round(deck)

  assert round.current_card() == card1

  turn = round.take_turn("Juneau")

  assert round.current_card() == card2

  assert round.turn_correct(turn) == True

  turn = round.take_turn("Nashville")

  assert round.current_card() == card3

  assert round.turn_correct(turn) == False

  assert len(round.turns) == 2

  assert round.turns[-1].feedback() == "Incorrect!!!!!!! >:["

def test_number_correct():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
               "Mars",
               "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
               "North north west",
               "STEM")
  cards = [card1, card2, card3]

  deck = Deck(cards)

  round = Round(deck)
  turn = round.take_turn("Juneau")
  turn = round.take_turn("Nashville")

  assert round.number_correct() == 1

def test_number_correct_by_category():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
               "Mars",
               "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
               "North north west",
               "STEM")
  cards = [card1, card2, card3]

  deck = Deck(cards)

  round = Round(deck)
  turn = round.take_turn("Juneau")
  turn = round.take_turn("Nashville")
  turn = round.take_turn("North north west")

  assert round.number_correct_by_category("STEM") == 1
  assert round.number_correct_by_category("Geography") == 1
  assert round.number_correct_by_category("Pop Culture") == 0

def test_percent_correct():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
               "Mars",
               "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
               "North north west",
               "STEM")
  cards = [card1, card2, card3]

  deck = Deck(cards)

  round = Round(deck)
  turn = round.take_turn("Juneau")
  turn = round.take_turn("Nashville")
  turn = round.take_turn("North north west")

  assert round.percent_correct() == 66.67

def test_percent_correct_by_category():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
               "Mars",
               "STEM")
  card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
               "North north west",
               "STEM")
  cards = [card1, card2, card3]

  deck = Deck(cards)

  round = Round(deck)
  turn = round.take_turn("Juneau")
  turn = round.take_turn("Nashville")
  turn = round.take_turn("North north west")

  assert round.percent_correct_by_category("Geography") == 100.00
  assert round.percent_correct_by_category("STEM") == 50.00