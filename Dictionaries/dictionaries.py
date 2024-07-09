
friends_ages = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "Diana": 28,
    "Eve": 27
}
print("Friends and their ages:", friends_ages)

student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Eve": 91
}

def update_score(student_name, new_score):
    if student_name in student_scores:
        student_scores[student_name] = new_score
        print(f"Updated {student_name}'s score to {new_score}.")
    else:
        print(f"Student {student_name} not found.")

update_score("Charlie", 95)

print("Updated student scores:", student_scores)