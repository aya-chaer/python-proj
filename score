# Students and their scores
students = {
    "Alice": 95,
    "Bob": 72,
    "Charlie": 58
}

# Function to calculate sum recursively
def sum_scores_recursive(scores):
    if len(scores) == 0:
        return 0
    return scores[0] + sum_scores_recursive(scores[1:])

# Extract scores as a list
scores = list(students.values())

# Calculate total and average using recursive sum
total_score = sum_scores_recursive(scores)
average_score = total_score / len(scores)

# Find top student
top_student = max(students, key=students.get)
top_score = students[top_student]

# List of students who scored below 60
failed_students = [name for name, score in students.items() if score < 60]

# Output
print("All students and scores:")
for name, score in students.items():
    print(f"{name} - {score}")

print(f"\nAverage score: {average_score}")
print(f"Top student: {top_student} ({top_score})")
print(f"Failed students: {', '.join(failed_students) if failed_students else 'None'}")
