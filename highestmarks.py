# Create a dictionary with 5 students and their marks
students = {
    "Riya": 78,
    "Aman": 45,
    "Sneha": 92,
    "Rahul": 50,
    "Priya": 38
}

# Display each student's name and marks using a loop
print("----- All Students -----")
for name, marks in students.items():
    print(f"{name}: {marks}")

# Display names of students who scored 50 or above
print("\n----- Scored 50 or Above -----")
for name, marks in students.items():
    if marks >= 50:
        print(name)

# Find and display the highest mark
highest = max(students.values())
print("\nHighest mark:", highest)