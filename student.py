from person import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.exercise = list()
    
    def __str__(self):
        return f"{self.first_name}{self.last_name} is in {self.cohort}. Their slack handle is {self.slack_handle}."

    