class Instructor:
    
    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):

        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.specialty = specialty

    def add_exercises(self, student, exercises):
        student.exercises.extend([exercises])