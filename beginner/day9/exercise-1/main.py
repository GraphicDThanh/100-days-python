student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key, value in student_scores.items():
  if value <= 70:
    student_grades[key] = "Fail"
    continue
  if value <= 80:
    student_grades[key] = "Acceptable"
    continue
    
  if value <= 90:
    student_grades[key] = "Exceeds Expectations"
    continue
    
  if value <= 100:
    student_grades[key] = "Outstanding"
    
# 🚨 Don't change the code below 👇
print(student_grades)
