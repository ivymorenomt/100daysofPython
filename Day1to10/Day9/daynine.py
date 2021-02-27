# Dictionary
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 76
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
print(student_grades)