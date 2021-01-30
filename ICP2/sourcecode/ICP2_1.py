
HeightInFeet = []                                     # List of student height in Feet
HeightInCms = []                                      # List of student height in Cms
students = int(input("Enter Number Of Students = "))  # User input for number of students
print("Enter the height of each student in feet = ")

for i in range(0, students):                          # Taking height in a feet for every student
    HeightInFeet.append(float(input()))

print("The student's height in Feet = ", HeightInFeet)

for j in range(students):
    HeightInCms.append(HeightInFeet[j] * 30.48)       # Formula for conversion

print("The student's height in Cms = ", HeightInCms)