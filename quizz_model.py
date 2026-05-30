
class QuizModel:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "answers": ["Paris", "Amsterdam", "Alger", "Brasil"],
                "correct": "Paris"
            }, 
            {
                "question": "Which planet is known as the Red Planet?",
                "answers": ["Mars", "Jupiter", "Venus", "Saturn"],
                "correct": "Mars"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "answers": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "correct": "Pacific Ocean"
            }
        ]
        self.current_index = 0
        self.score = 0

    def get_current_question(self):
        return self.questions[self.current_index]["question"]

    def check_answer(self, answer):
        if answer == self.questions[self.current_index]["correct"]:
            self.score += 1 
            return True
        return False