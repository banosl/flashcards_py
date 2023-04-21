class Card:
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer.lower()
        self.category = category