# Employee Attendance Management System by Mahendra

FILE_NAME = "attendance.txt"


def mark_attendance():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    status = input("Enter Attendance (Present/Absent): ").capitalize()

    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id},{name},{status}\n")

    print("Attendance recorded successfully!\n")


def view_attendance():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        if not records:
            print("No attendance records found.\n")
            return

        print("\n--- Attendance Records ---")
        for record in records:
            emp_id, name, status = record.strip().split(",")
            print(f"ID: {emp_id}, Name: {name}, Status: {status}")
        print()

    except FileNotFoundError:
        print("No attendance file found.\n")


def attendance_report():
    total = 0
    present = 0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                total += 1
                if "Present" in line:
                    present += 1

        if total == 0:
            print("No data to generate report.\n")
            return

        percentage = (present / total) * 100
        print(f"\nTotal Records: {total}")
        print(f"Present Count: {present}")
        print(f"Attendance Percentage: {percentage:.2f}%\n")

    except FileNotFoundError:
        print("No attendance file found.\n")


def main_menu():
    while True:
        print("=== Employee Attendance Management ===")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Attendance Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            attendance_report()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")



main_menu()
