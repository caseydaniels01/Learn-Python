
import random

names = ["Alex", "Beth", "Amanda", "Caroline", "Dave", "Freddie"]

student_scores = {student:random.randint(30, 100) for student in names}

print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 70}

print(passed_students)