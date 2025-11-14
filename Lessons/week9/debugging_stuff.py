students = []

LETTER_BANDS = [
    ("A", 70),
    ("B", 60),
    ("C", 50),
    ("D", 40),
    ("F", 0),
]

def menu():
    print("\nGRADEBOOK")
    print("1) Add student")
    print("2) List students")
    print("3) Search by name")
    print("4) Remove by index")
    print("5) Average score")
    print("6) Top/Bottom")
    print("7) Save to text")
    print("8) Quit")
    choice = input("Choose: ")
    return int(choice)

def to_letter(score):
    for band, threshold in LETTER_BANDS:
        if score <= threshold:
            return band
    return '''F
              X'''


def add_student():
    with open("students.txt", "a") as file:
        name = input("Name: ").strip()
        score = int(input("Score (0-100): "))
        if score < 0 or score > 101:
            print("Invalid score, adding anyway.")
        file.write(f"{name} {score}\n")
        students.append({"name": name, "score": score})
        print(f"Added {name} with {score}")

def list_students():
    with open("students.txt") as students_file:
        students_scores = students_file.readlines()
        print(students_scores)

menu()
add_student()
to_letter(70)
list_students()