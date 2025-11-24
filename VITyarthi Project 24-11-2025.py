import os
import csv

ATTENDANCE_FILE = "attendance.csv"

students = [
    {"name": "Hitansh", "reg_no": "25BCE11001"},
    {"name": "Vinayak", "reg_no": "25BCE11002"},
    {"name": "yogya", "reg_no": "25BCE11003"},
]

attendance_records = []


def load_attendance():
    global attendance_records, students
    
    if not os.path.exists(ATTENDANCE_FILE):
        attendance_records = []
        return

    attendance_records = []
    existing_reg_nos = {s["reg_no"] for s in students} 

    try:
        with open(ATTENDANCE_FILE, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "registration_number" in row:
                    reg_no = row["registration_number"]
                    
                    record = {
                        "name": row.get("name", "Unknown"),
                        "reg_no": reg_no,
                        "date": row["date"],
                        "attendance": row["attendance"],
                    }
                    attendance_records.append(record)
                    
                    if reg_no not in existing_reg_nos:
                        students.append({"name": record["name"], "reg_no": reg_no})
                        existing_reg_nos.add(reg_no)
    except Exception as e:
        print(f"Warning: Could not load file completely. Data might be corrupted. ({e})")
        
def save_attendance():
    with open(ATTENDANCE_FILE, mode="w", newline="") as f:
        fieldnames = ["name", "registration_number", "date", "attendance"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for record in attendance_records:
            writer.writerow({
                "name": record["name"],
                "registration_number": record["reg_no"],
                "date": record["date"],
                "attendance": record["attendance"],
            })


def find_student_by_input(user_input: str):
    
    for s in students:
        if s["reg_no"].upper() == user_input.upper():
            return s["name"], s["reg_no"]
    
    for s in students:
        if s["name"].lower() == user_input.lower():
            return s["name"], s["reg_no"]

    return None, None


def mark_todays_attendance():
    global attendance_records

    print("\n--- Mark Today's Attendance ---")
    today = input("Enter today's date (DD-MM-YYYY): ").strip()
    
    if len(today) != 10:
        print("Date format looks incorrect (must be 10 characters). Please re-run if wrong.")
    if not today:
        print("Date cannot be empty.")
        return

    if not students:
        print("No students defined. Cannot mark attendance.")
        return

    print("\nEnter 'P' for Present and 'A' for Absent.\n")

    temp_records = []
    for r in attendance_records:
        if r["date"] != today:
            temp_records.append(r)
    attendance_records = temp_records

    for index, s in enumerate(students, start=1):
        while True:
            status = input(f"{index}. {s['name']} ({s['reg_no']}): ").strip() 
            
            if status.upper() in ("P", "A"):
                attendance_records.append(
                    {
                        "name": s["name"],
                        "reg_no": s["reg_no"],
                        "date": today,
                        "attendance": status.upper(),
                    }
                )
                break
            else:
                print("Invalid input. Please enter only 'P' or 'A'.")

    save_attendance()
    print(f"\nAttendance for {today} saved successfully.")


def check_class_attendance():
    print("\n--- Check Attendance of Class ---")
    date_str = input("Enter date (DD-MM-YYYY): ").strip()

    if not date_str:
        print("Date cannot be empty.")
        return

    date_attendance = {}
    for r in attendance_records:
        if r["date"] == date_str:
            date_attendance[r["reg_no"]] = r["attendance"]
            
    print(f"\nAttendance for {date_str}:")
    print("{:<6} {:<20} {:<15} {:<10}".format("S.No", "Name", "Reg No", "Status"))
    print("-" * 60)

    any_marked = bool(date_attendance)

    for index, s in enumerate(students, start=1):
        status = date_attendance.get(s["reg_no"], "Not marked")
        
        print("{:<6} {:<20} {:<15} {:<10}".format(index, s["name"], s["reg_no"], status))

    if not any_marked:
        print("\nNo attendance records found for this date.")


def check_student_attendance():
    print("\n--- Check Attendance of Student ---")
    user_input = input("Enter student's name or registration number: ").strip().lower() 
    date_str = input("Enter date (DD-MM-YYYY): ").strip()

    if not user_input or not date_str:
        print("Both student and date are required.")
        return

    name, reg_no = find_student_by_input(user_input)
    if name is None:
        print("No student found with that name or registration number.")
        return

    found_record = False
    for r in attendance_records:
        if r["reg_no"] == reg_no and r["date"] == date_str:
            print(f"\nOn {date_str}, {name} ({reg_no}) was: {r['attendance']}")
            found_record = True
            break
            
    if not found_record:
        print(f"\nNo attendance record found for {name} ({reg_no}) on {date_str}.")


def update_student_attendance():
    global attendance_records

    print("\n--- Update Attendance of Student ---")
    user_input = input("Enter student's name or registration number: ").strip()
    date_str = input("Enter date (DD-MM-YYYY) to update: ").strip()

    if not user_input or not date_str:
        print("Both student and date are required.")
        return

    name, reg_no = find_student_by_input(user_input)
    if name is None:
        print("No student found with that name or registration number.")
        return

    target_record = None
    for r in attendance_records:
        if r["reg_no"] == reg_no and r["date"] == date_str:
            target_record = r
            break

    if target_record is None:
        print("No existing attendance record found for that student on that date.")
        return

    print(
        f"Current attendance for {name} ({reg_no}) on {date_str}: "
        f"{target_record['attendance']}"
    )

    while True:
        new_status = input("Enter new attendance (P/A): ").strip().upper()
        if new_status in ("P", "A"):
            target_record["attendance"] = new_status
            save_attendance()
            print("Attendance updated successfully.")
            break
        else:
            print("Invalid input. Please enter only 'P' or 'A'.")


def update_student_details_by_serial():
    global students, attendance_records

    if not students:
        print("\nNo students available to update.")
        return

    print("\n--- Update Student Details (by Serial Number) ---")
    print("{:<6} {:<20} {:<15}".format("S.No", "Name", "Reg No"))
    print("-" * 45)
    for index, s in enumerate(students, start=1):
        print("{:<6} {:<20} {:<15}".format(index, s["name"], s["reg_no"]))

    serial_input = input("\nEnter the serial number of the student to update: ").strip()
    
    if not serial_input.isdigit():
        print("Invalid serial number.")
        return

    serial = int(serial_input)
    if serial < 1 or serial > len(students):
        print("Serial number out of range.")
        return

    student = students[serial - 1]
    old_name = student["name"]
    old_reg_no = student["reg_no"]

    print(f"\nCurrent details for S.No {serial}: Name: {old_name}, Reg No: {old_reg_no}")

    new_name = input("Enter new name (leave blank to keep unchanged): ").strip()
    new_reg_no = input(
        "Enter new registration number (10 characters, leave blank to keep unchanged): "
    ).strip()

    if new_reg_no and len(new_reg_no) != 10:
        print("Registration number must be exactly 10 characters. Update cancelled.")
        return

    if new_name:
        student["name"] = new_name
    if new_reg_no:
        student["reg_no"] = new_reg_no

    for r in attendance_records:
        if r["reg_no"] == old_reg_no:
            if new_name:
                r["name"] = new_name
            if new_reg_no:
                r["reg_no"] = new_reg_no

    save_attendance()
    print("\nStudent details updated successfully.")


def add_new_students():
    global students

    print("\n--- Add New Students ---")

    while True:
        name = input("Enter student name (or press Enter to stop): ").strip()
        if not name:
            print("Stopped adding students.")
            break

        reg_no = input("Enter registration number (10 characters): ").strip().upper()
        if len(reg_no) != 10:
            print("Registration number must be exactly 10 characters. Student not added.")
            continue

        if any(s["reg_no"].upper() == reg_no for s in students):
            print("A student with this registration number already exists. Not added.")
        else:
            students.append({"name": name, "reg_no": reg_no})
            print(f"Student {name} added.")

        cont = input("Do you want to add another student? (Y/N, default is Y): ").strip().upper()
        if cont == "N":
            print("Finished adding students.")
            break


def main_menu():
    while True:
        print("\n===== VITyarthi Attendance Project =====")
        print("1. Mark today's attendance")
        print("2. Check attendance of class")
        print("3. Check attendance of student")
        print("4. Update attendance of student")
        print("5. Update student details")
        print("6. Add new students")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            mark_todays_attendance()
        elif choice == "2":
            check_class_attendance()
        elif choice == "3":
            check_student_attendance()
        elif choice == "4":
            update_student_attendance()
        elif choice == "5":
            update_student_details_by_serial()
        elif choice == "6":
            add_new_students()
        elif choice == "7":
            print("Exiting application. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    load_attendance()
    main_menu()