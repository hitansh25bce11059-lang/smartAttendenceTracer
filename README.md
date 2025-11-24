**VITyarthi Attendance Tracker**

- **Project:** : Simple CLI attendance tracker for small classes
- **Main script:** `VITyarthi Project 24-11-2025.py`
- **Data file:** `attendance.csv`

**Overview**
- **Purpose:** A lightweight Python command-line application to record, view, and update student attendance. It stores attendance records in a CSV file and allows identification of students by name or registration number. The program is designed for small-class use and quick manual entry.

**Features**
- **Mark today's attendance:** Prompt-driven entry to mark each student as Present (`P`) or Absent (`A`) for a specified date. Replaces any existing records for the same date to avoid duplicates.
- **Check class attendance:** View the entire class attendance status for any date in a formatted table. If a student has no record for the date, they show as `Not marked`.
- **Check student attendance:** Query a single student's attendance for a given date using either their registration number or name (case-insensitive lookup).
- **Update attendance of student:** Modify an existing attendance entry (for a specific student and date) from `P` to `A` or vice versa.
- **Update student details (by serial number):** Rename a student or change their registration number; updates all related attendance records to preserve consistency.
- **Add new students:** Interactive loop to add one or more students. Registration numbers are validated to be exactly 10 characters and are stored uppercase.
- **CSV persistence:** All attendance records are saved in `attendance.csv` with columns: `name`, `registration_number`, `date`, `attendance`.
- **Robust loading:** The loader attempts to handle missing CSV gracefully and will warn on read errors rather than crash.

**Data format (CSV)**
- Header: `name,registration_number,date,attendance`
- Example row: `Hitansh,25BCE11059,24-11-2025,P`
- `date` format: `DD-MM-YYYY` (the program expects this format when reading/writing and when prompting the user)
- `attendance` values: `P` (Present) or `A` (Absent)

**Validation & Behavior**
- **Registration number:** When adding or updating a student, registration numbers must be exactly 10 characters; new registration numbers are converted to uppercase.
- **Attendance input:** Only `P` or `A` (case-insensitive on input) are accepted when marking or updating attendance.
- **Date input:** The app expects a 10-character date string in `DD-MM-YYYY`. It performs minimal format checks; you should enter dates in the expected format.
- **Student lookup:** The app searches first by registration number (case-insensitive) then by name (case-insensitive). If multiple students have the same name, the registration number lookup is recommended.

**How to run**
- Make sure you have Python 3 installed.
- Open a PowerShell terminal in the project folder (where `VITyarthi Project 24-11-2025.py` is located).

Example command (PowerShell):
```powershell
python "VITyarthi Project 24-11-2025.py"
```

When you run the script you will see a text menu with options:
- `1` Mark today's attendance
- `2` Check attendance of class
- `3` Check attendance of student
- `4` Update attendance of student
- `5` Update student details
- `6` Add new students
- `7` Exit

Follow on-screen prompts for each option. Inputs are interactive.

**Example usage flows**
- Mark attendance for a date `24-11-2025` by choosing option `1` and then entering `P` or `A` for each listed student.
- Check the class for `24-11-2025` using option `2` to get a tabular display.
- Update a mistaken entry by choosing option `4`, providing student id/name and date, then entering the corrected `P`/`A` value.

**File structure**
- `VITyarthi Project 24-11-2025.py` : Main Python script (CLI application).
- `attendance.csv` : CSV file used to persist attendance data. Created automatically when saving the first attendance.

**Implementation notes**
- `load_attendance()` reads `attendance.csv` if present, and integrates any registration numbers not present in the in-memory `students` list.
- `save_attendance()` writes the entire in-memory `attendance_records` back to `attendance.csv` (includes header row).
- Student changes (name or reg no) are propagated to historical records so attendance history stays consistent.

**Limitations & Suggested Improvements**
- Date validation is minimal — consider using `datetime.strptime` to enforce and parse dates.
- Input is entirely synchronous via the terminal; a GUI or web interface would be more user friendly for larger classes.
- CSV is used for simplicity; migrating to SQLite would improve concurrency and data integrity for multi-user use.
- Add unit tests to verify save/load/update behaviors and edge cases.

**Contributing**
- Feel free to open issues or submit pull requests. For code style, maintain the existing simple procedural style or propose a refactor with tests.

**License**
- This project currently has no explicit license file. Add a `LICENSE` with the appropriate terms before publishing.

**Contact**
- For questions or improvements, reach out to the project author (local repository owner) or create an issue in the repo.

---
Generated README for `VITyarthi Project 24-11-2025.py` — keep this file next to the script and `attendance.csv` for best results.

**Project Title**

- **VITyarthi Attendance Tracker**

**Overview of the project**

- VITyarthi Attendance Tracker is a lightweight command-line Python application for recording, viewing and updating student attendance. It is aimed at small classes or single-instructor scenarios where a simple CSV-backed persistence layer is sufficient. The application lists students, prompts for attendance (Present/Absent) for a given date, and stores the results in `attendance.csv`.

**Features**

- Mark today's attendance (interactive; accepts `P`/`A`).
- Check class attendance for any date (tabular view).
- Check a single student's attendance for a date (lookup by registration number or name).
- Update an individual student's attendance record for a specific date.
- Update student details (name and registration number) by serial number; updates historical attendance entries accordingly.
- Add new students with registration number validation (exactly 10 characters).
- CSV-based persistence with a header and safe load/save behaviors.

**Technologies / Tools Used**

- Python 3.8+ (standard library only required for running the current script).
- Built-in modules: `csv`, `os`.
- Optional (for improved testing/development): `pytest` for unit testing.

**Steps to install & run the project**

1. Install Python 3.8 or newer (https://www.python.org/downloads/).
2. (Optional but recommended) Create and activate a virtual environment.

PowerShell example (Windows):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

3. Run the app from the project folder:
```powershell
python "VITyarthi Project 24-11-2025.py"
```

Notes:
- The application will create `attendance.csv` when saving attendance for the first time.
- Keep the `VITyarthi Project 24-11-2025.py` script and `attendance.csv` in the same folder.

**Instructions for testing**

Manual testing (quick smoke tests):
- Start the script and select option `1` to mark attendance for a date. Enter `P`/`A` for each listed student and verify `attendance.csv` has been created/updated.
- Use option `2` to view class attendance for the date used above.
- Use option `3` and provide a name or registration number + the date to verify a single record.
- Intentionally enter invalid values (e.g., wrong reg no length, invalid attendance letters like `X`) to confirm validation messages are shown.

Automated testing (recommended):
- The repository does not include unit tests by default. To add tests, install `pytest` in your virtual environment and write tests that exercise `load_attendance()`, `save_attendance()` and the pure functions such as `find_student_by_input()`.

Example commands to run tests after adding them:
```powershell
python -m pip install pytest
pytest -q
```

Test suggestions:
- Create a temporary CSV file fixture and assert `load_attendance()` reads rows correctly.
- Test `save_attendance()` writes expected headers and rows.
- Test student-update flows: renaming a student and ensuring attendance records reflect the change.

**Screenshots (optional)**

- Add screenshots to a `screenshots/` folder and reference them in this README. Example markup to include an image:

```markdown
![Main menu screenshot](screenshots/menu.png)
```

Small inline example of the CLI menu (text):

```
===== VITyarthi Attendance Project =====
1. Mark today's attendance
2. Check attendance of class
3. Check attendance of student
4. Update attendance of student
5. Update student details
6. Add new students
7. Exit
```

**Where to file issues / contribute**

- Create issues or pull requests against this repository for bug reports or feature suggestions. If you submit code, please include tests and keep changes focused.

**Further improvements (suggested)**

- Enforce strict date parsing using `datetime.strptime` to avoid malformed dates.
- Add a small SQLite backend or use `pandas` for more robust storage and analysis.
- Add unit tests and CI (GitHub Actions) to run tests automatically on push/PR.
- Add a GUI or web frontend for easier use in real classrooms.

---
If you want, I can create an example `attendance.csv` and a `screenshots/` folder with a sample screenshot placeholder. Tell me which you'd like next.

