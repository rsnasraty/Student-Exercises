from person import NSSPerson

class Student(NSSPerson):
    def __init__(self, first, last, slack, cohort):
        super().__init__(first, last, slack, cohort)
        self.exercise = list()
    
    def __str__(self):
        return f"{self.first}{self.last} is in {self.cohort}. Their slack handle is {self.slack}."

    