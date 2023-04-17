from lib.card import Card

#card exists and has attributes
def test_card():
    c = Card("What is the capital of Alaska?", "Juneau", "Geography")
    assert c.question == "What is the capital of Alaska?"
    assert c.answer == "Juneau"
    assert c.category == "Geography"