"""
This class holds question model for question details.
"""

QUESTIONS = []
class Question():
    class_count = 1
    def __init__(self):
        self.title = None
        self.body = None
        self.createdOn=None
        self.user_id = None
        self.meetup_id = None
        self.question_id = Question.class_count
        Question.class_count_=1
