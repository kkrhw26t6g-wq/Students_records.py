def add_student(students):
    """Option 1: Collects student details and appends record dictionary to list."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be a positive integer.")
            return
    except ValueError:
        print("Error: Please enter a valid integer for number of scores.")
        return

    scores = []
    for i in range(1, num_scores + 1):
        try:
            score = float(input(f"Enter score {i}: "))
            scores.append(score)
        except ValueError:
            print("Error: Please enter a numeric score.")
            return

    student_record = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student_record)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Option 2: Displays all student records in a formatted table."""
    if not students:
        print("No student records found.")
        return

    print("----------------------------------------------------------------")
    print(f"{'Name':<18} {'ID':<12} {'Scores':<15} {'Average':<8}")
    print("----------------------------------------------------------------")

    for student in students:
        scores_list = student["scores"]

        # Calculate average using total_score variable name
        if scores_list:
            total_score = 0
            for score in scores_list:
                total_score += score
            avg = total_score / len(scores_list)
        else:
            avg = 0.0

        scores_str = ", ".join(
            str(int(s)) if s.is_integer() else str(s) for s in scores_list
        )

        print(f"{student['name']:<18} {student['id']:<12} {scores_str:<15} {avg:.2f}")

    print("----------------------------------------------------------------")


def calculate_student_average(students):
    """Option 3: Finds a specific student by ID and prints their average score."""
    search_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == search_id:
            scores_list = student["scores"]
            if scores_list:
                total_score = 0
                for score in scores_list:
                    total_score += score
                avg = total_score / len(scores_list)
            else:
                avg = 0.0

            print(f"{student['name']}'s average score: {avg:.2f}")
            return

    print(f"Error: Student ID '{search_id}' not found.")


def display_menu():
    """Prints the main menu interface."""
    print("\n===============================")
    print("  STUDENT RECORD SYSTEM MENU  ")
    print("===============================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()