# 9.1 Excercise
# Open the file in write mode
with open("grades.txt", "w") as file:
    while True:
        grade = input("Enter a grade (-1 to stop): ")
        
        # Check for sentinel value
        if grade == "-1":
            break
        
        file.write(grade + "\n")  # Write the grade to the file

print("Grades saved to grades.txt.")

#9.2 Excercise
# Initialize variables
total = 0
count = 0

# Open and read the file
with open("grades.txt", "r") as file:
    grades = file.readlines()  # Read all lines into a list

# Process the grades
print("Grades:")
for grade in grades:
    grade = int(grade.strip())  # Convert to an integer
    print(grade)
    total += grade
    count += 1

# Calculate the average
average = total / count if count > 0 else 0

# Display results
print("\nTotal:", total)
print("Count:", count)
print("Average:", round(average, 2))

#9.3 Exercise
import csv

# Open the CSV file in write mode
with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])

    # Collect student data
    while True:
        first_name = input("Enter first name (or type 'exit' to stop): ")
        if first_name.lower() == "exit":
            break
        
        last_name = input("Enter last name: ")
        exam1 = int(input("Enter first exam grade: "))
        exam2 = int(input("Enter second exam grade: "))
        exam3 = int(input("Enter third exam grade: "))

        # Write student record to file
        writer.writerow([first_name, last_name, exam1, exam2, exam3])

print("Student records saved to grades.csv.")
