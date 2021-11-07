
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
counter = 0

for student_height in student_heights:
  total_height = total_height + student_height
  counter = counter + 1

average = total_height / counter

print(f"The average of students height is {average}")


