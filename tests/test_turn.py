from lib.card import Card
from lib.turn import Turn

def test_turn():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  turn1 = Turn("Juneau", card1)

  assert turn1.guess == "Juneau"
  assert turn1.card == card1

  turn1 = Turn("Honolulu", card1)
  assert turn1.guess != "Bob"

def test_check_correct():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  turn1 = Turn("Juneau", card1)
  turn2 = Turn("Honolulu", card1)
  
  result = turn1.check_correct()
  assert result == True

  result = turn2.check_correct()
  assert result == False

def test_feedback():
  card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
  turn1 = Turn("Juneau", card1)
  turn2 = Turn("Honolulu", card1)

  result = turn1.feedback()
  assert result == "Correct!"

  result = turn2.feedback()
  assert result == "Incorrect!!!!!!! >:["