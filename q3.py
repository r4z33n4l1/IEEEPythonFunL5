
'''
    Define a function named analyze_students that accepts two parameters:

    students: a list of dictionaries, where each dictionary contains information 
      about a student in the format {'name': 'John', 'grades': [85, 90, 92], 'age': 16}.

    grade_threshold: a float representing a grade threshold, default value should be 90.0.

    This function should perform the following tasks:

    Calculate the average grade for each student and add it to their dictionary with the key 'average_grade'.
    Count and return the number of students whose average grade is above the grade_threshold.
    
    Also, return a list of students who are above the grade_threshold,
'''
 
 
def analyze_students(students, grade_threshold=90.0):
    above_threshold = []
    for student in students:
        average_grade = sum(student['grades']) / len(student['grades'])
        student['average_grade'] = average_grade
        if average_grade > grade_threshold:
            above_threshold.append(student)
    return len(above_threshold), above_threshold

students = [{'name': 'John', 'grades': [85, 90, 92], 'age': 16},
            {'name': 'Jane', 'grades': [95, 96, 97], 'age': 15},
            {'name': 'Bob', 'grades': [80, 82, 84], 'age': 16}]

number, student_list = analyze_students(students)
print(f'Number of students above threshold: {number}')
for student in student_list:
    print(student)
