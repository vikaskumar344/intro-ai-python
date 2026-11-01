def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Needs improvement"


student_name = "Your Name"
subjects = ["Python", "Mathematics", "English"]
marks = [85, 78, 92]

print("STUDENT MARKS ANALYZER")
print("Student:", student_name)

for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")

average = calculate_average(marks)

print(f"\nAverage: {average:.2f}")
print("Grade:", get_grade(average))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
