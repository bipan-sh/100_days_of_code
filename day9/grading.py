student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

students_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score > 90:
        students_grades[key] = "A"
    if score > 80:
        students_grades[key] = "B"
    if score > 70:
        students_grades[key] = "C"
    else:
        students_grades[key] = "F"

print(students_grades)


#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
#print(student_grades)