from person import NSSPerson

class Instructor:
    
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        super().__init__(first_name,last_name, slack_handle,  cohort)
        self.specialty = specialty

    def add_exercises(self, student, exercise):
        student.exercise.extend([exercise])