students = []
def add_student():
    name = input("enter a name of studend:")
    marks = []
    subjects = ["python","english","computer","math"]
    for subject in subjects:
        mark =float(input(f"enter a marks for {subject}"))
        marks.append(mark)

    total = sum(marks)
    percentage = total / len(subjects)

    if percentage >= 90:
        grade = "A+"

    elif percentage>= 80:
        grade = "A"

    elif percentage>= 70:
        grade = "B"

    elif percentage>= 60:
        grade = "C"

    elif percentage >= 40:
        grade = "D"

    else:
        grade = "F"


    student = { "name" : name,
            "marks"  : marks,
            "percentage" : percentage,
            "total" : total,
            "grade"  : grade
 
      }
    students.append(student)

    print("students added successfuly \n")


def show_student():
    if not students:
        print("no student found")
        return
    for student in students:
        print(" \n student perfromer analyzeer")

        print(f"\nNAME: {student['name']}")
        print(f"TOTAL MARKS: {student['marks']}")
        print(f"total marks: {student['total']}")
        print(f"Total Percentage: {student['percentage']}")
        print(f"grade :{student['grade']}")

def show_top_student():

    if not students:
        print("not student available")
        return
    top_student = max(students , key = lambda student : student["percentage"])
    print("\n--- Top Student ---")
    print(f"Name: {top_student['name']}")
    print(f"Percentage: {top_student['percentage']:.2f}%")
    print(f"Grade: {top_student['grade']}")


def class_average():
    if not students:
        print("No student records found.\n")
        return

    average = sum(
        student["percentage"] for student in students
    ) / len(students)

    print(f"\nClass Average: {average:.2f}%")


while True:

    print("\nstudent performance analyzer!!")
    print("enter 1 to add student")
    print("enter 2 to show student")
    print("enter 3 to show top student")
    print(" enter 4 to show class average")
    print("enter 5 to exit")

    choice  = input("enter a choices :")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_student()

    elif choice == "3":
        show_top_student()

    elif choice == "4":
        class_average()

    elif choice == "5":
        print("any key to exit")
        break
    else:
        print("invalid !!")
        






