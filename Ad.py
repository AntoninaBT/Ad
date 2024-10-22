# Teplova // An average score for students.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5] ]#list
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #set
# Find an average score. Create a variable and refer to each index in the list (grades) with sum and len
average = (sum(grades[0]) / len(grades[0]),
           sum(grades[1]) / len(grades[1]),
           sum(grades[2]) / len(grades[2]),
           sum(grades[3]) / len(grades[3]),
           sum(grades[4]) / len(grades[4]))
print(average)
# Create a dictionary. Change a set to a list, use method "list'
students_list = list(students)
print(students_list)
# Sort the list
students_list_sort = sorted(students_list)
print(students_list_sort)
# Create a dictionary with method dict and connect students and grades with method zip
students_grades = dict(zip(students_list_sort, average))
print(students_grades)