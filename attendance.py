"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}   

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id not in attendance:
        attendance[student_id] = {
            "name": name,
            "records": {}
        }
        print(f"Student {name} (ID: {student_id}) registered.")
    else:
        print(f"Student ID {student_id} already exists.")


def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    for student_id in student_ids:
        if student_id in attendance:
            attendance[student_id]["records"][today] = "Present"
        else:
            print(f"Student ID {student_id} not found.")


def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    for student_id in student_ids:
        if student_id in attendance:
            attendance[student_id]["records"][today] = "Absent"
        else:
            print(f"Student ID {student_id} not found.")


def get_report(date=None, student_id=None):
    """
    Generate attendance report with optional filters.
    - date: filter by specific date
    - student_id: filter by specific student
    """
    report = {}

    for sid, data in attendance.items():
        if student_id and sid != student_id:
            continue

        if date:
            # Report for a specific date
            report[sid] = {
                "name": data["name"],
                "status": data["records"].get(date, "Not Recorded")
            }
        else:
            # Full history
            report[sid] = {
                "name": data["name"],
                "records": data["records"]
            }

    return report


# ==== Example usage ====
register_student(1, "Alice")
register_student(2, "Bob")
register_student(3, "Charlie")

mark_present([1, 2])
mark_absent([3])

print("\nFull Report:")
print(get_report())

print("\nReport for today only:")
print(get_report(date=str(datetime.date.today())))

