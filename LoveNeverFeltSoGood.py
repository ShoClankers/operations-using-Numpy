
import numpy as np

FILE_NAME = "student_records.txt"


def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    fav_subject = input("Enter Favourite Subject: ")
    intro = input("Enter a Brief Introduction: ")


    student_id_array = np.array([student_id])

    with open(FILE_NAME, "a") as file:
        file.write(
            f"ID: {student_id_array[0]}, "
            f"Name: {name}, "
            f"Favourite Subject: {fav_subject}, "
            f"Introduction: {intro}\n"
        )

    print("Student record added successfully!\n")


# Function to display all records
def display_records():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()

        if data:
            print("\n----- Student Records -----")
            print(data)
        else:
            print("No records found.")

    except FileNotFoundError:
        print("Record file does not exist yet.")



def count_students():
    try:
        ids = []

        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.split(",")
                student_id = int(parts[0].split(":")[1].strip())
                ids.append(student_id)

        id_array = np.array(ids)
        print(f"\nTotal Students Recorded: {id_array.size}")

    except FileNotFoundError:
        print("No records available.")



while True:
    print("\n===== Roy's Student Record System =====")
    print("1. Add Student")
    print("2. View Records")
    print("3. Count Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_records()
    elif choice == "3":
        count_students()
    elif choice == "4":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Try again.")