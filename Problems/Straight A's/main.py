# put your python code here
students_grades = (input()).split()


def count_prop(grades):
    num_of_grades = 0.0
    num_of_a = 0.0
    for grade in grades:
        if grade == 'A':
            num_of_a += 1.0
        num_of_grades += 1.0
    proportion = num_of_a / num_of_grades
    return round(proportion, 2)


grade_prop = count_prop(students_grades)
print(grade_prop)
