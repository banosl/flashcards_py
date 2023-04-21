from lib.card import Card
from lib.deck import Deck
from lib.turn import Turn
from lib.round import Round
    
card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
              "Mars",
              "STEM")
card3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?",
              "North north west",
              "STEM")
card4 = Card("What is pi?",
              "3.14",
              "STEM")
card5 = Card("What is the capital of Canada?",
              "Ottawa",
              "Geography")
card6 = Card("What's Miley Cyrus' alter ego?",
              "Hannah Montana",
              "Pop culture")
cards = [card1, card2, card3, card4, card5, card6]

deck = Deck(cards)

round = Round(deck)


def question_loop(cards, round, counter, cards_count):
  print("-------------------------------------------------")
  print(f"This is card number {counter} out of {cards_count}.")
  print(f"Question: {round.current_card().question}")

  answer = input()

  round.take_turn(answer)
  print(round.turns[len(round.turns)-1].feedback())




def start(cards, round):
  cards_count = len(cards)
  counter = 0
  counter += 1
  print(f"Welcome! You're playing with {cards_count} cards.")
  while (counter < (cards_count + 1)):
    question_loop(cards, round, counter, cards_count)
    counter += 1
start(cards, round)
