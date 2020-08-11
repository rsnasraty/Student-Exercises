from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

"""
Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

Create 4, or more, exercises.
Create 3, or more, cohorts.
Create 4, or more, students and assign them to one of the cohorts.
Create 3, or more, instructors and assign them to one of the cohorts.
Have each instructor assign 2 exercises to each of the students.
"""


petting_zoo = Exercise("Petting Zoo", "Python")
cash_4_coins = Exercise("Cash 4 Coins", "Python")
kennel = Exercise("Kennel", "React")
planets = Exercise("Planets", "Python")
coins_4_cash = Exercise("Coins 4 Cash", "Python")

c40 = Cohort("Cohort 40")
c38 = Cohort("Cohort 38")
c41 = Cohort("Cohort 41")

roxanne = Student("Roxanne", "Nasraty", "foxy_roxy", c40)
makoto = Student("Makoto", "Tachibana", "tachibana_coach", c41)
haru  = Student("Haru", "Nanase", "swim_free", c41)
kylo = Student("Kylo", "Ren", "vader_stan", c38)
rey  = Student("Rey", "Nobody", "the_scavenger", c38)

joe = Instructor("Joe", "Shepherd", "banAgazon", "sass", c40)
bryan = Instructor("Bryan", "Nilsen", "bry5", "jokes", c41)
madi = Instructor("Madi", "Peper", "pepperpotts", "voice of the people", c38)

c40.students.extend([roxanne])
c41.students.extend([makoto, haru])
c38.students.extend([kylo, rey])

c40.instructors.extend([joe])
c41.instructors.extend([bryan])
c38.instructors.extend([madi])

joe.add_exercises(roxanne, [planets, cash_4_coins])
bryan.add_exercises(haru, [petting_zoo, kennel])
madi.add_exercises(kylo, [coins_4_cash, cash_4_coins])
