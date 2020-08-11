from person import NSSPerson

class Instructor:
    
    def __init__(self, first, last, slack, cohort, specialty):
        super().__init__(first,last, slack, cohort)
        self.specialty = specialty

    def add_exercises(self, student, exercise):
        student.exercise.extend([exercise])