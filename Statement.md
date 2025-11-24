Problem Statement
-----------------

Managing student attendance for small classes and labs is often performed manually on paper or with ad-hoc spreadsheets. These methods are error-prone, difficult to update consistently, and do not provide a simple command-line workflow for quick marking, querying, or correcting of attendance records. Instructors need a lightweight, low-dependency tool that lets them record, view, and update attendance reliably and persistently.

Scope of the Project
--------------------

- Provide a minimal, stable command-line attendance application that requires only Python and the standard library.
- Persist attendance data to a CSV file (`attendance.csv`) using a simple, documented schema: `name,registration_number,date,attendance`.
- Support marking attendance for a date, listing class attendance for a date, querying an individual student's attendance for a date, updating a recorded attendance entry, and managing student details (add/update).
- Ensure reasonable input validation (registration number length, attendance values restricted to `P` or `A`, simple date-format checks) and avoid crashes on missing or corrupted CSV files by using safe load/save operations and user-facing warnings.
- Keep the application single-user and synchronous (terminal-based); no network, concurrency, or multi-user editing features are included.

Out of scope (explicitly excluded)
----------------------------------

- Real-time multi-user access, concurrency control, or remote syncing.
- A web or graphical user interface (though these are suggested as future improvements).
- Advanced analytics or reporting beyond date-by-date attendance lookup.
- Complex scheduling, multiple classes per CSV, or automatic calendar integration.

Target Users
------------

- Individual instructors and teaching assistants who manage attendance for small classes or lab sessions.
- Small training programs, study groups, or project teams that need a lightweight attendance record-keeping tool.
- Students or hobbyist developers who want a simple sample project demonstrating CSV persistence and basic CLI interactions.

High-level Features
-------------------

- Interactive CLI menu for the following operations:
  - Mark today's attendance: prompt each listed student and record `P` (Present) or `A` (Absent) for a given date. Replaces any existing records for the same date to avoid duplication.
  - Check attendance of class: show a formatted table of all students and their status for a requested date (shows `Not marked` where no record exists).
  - Check attendance of student: lookup a single student's attendance by registration number or name for a specific date.
  - Update attendance of student: change an existing attendance entry (for a given student and date) from `P` to `A` or vice versa.
  - Update student details (by serial number): rename a student or change their registration number and propagate these changes to historical attendance records.
  - Add new students: interactively add students with registration number validation (exact 10 characters, stored uppercase).

- CSV persistence: read/write `attendance.csv` with headers and defensive handling of missing or malformed files.
- Case-insensitive student lookup (registration number prioritized, then name).

Assumptions & Constraints
------------------------

- Dates are entered and displayed using the `DD-MM-YYYY` format; date parsing is minimally validated by string length in the current implementation.
- Registration numbers are expected to be a 10-character identifier (validated on add/update flows).
- The tool is intended for single-user, manual operation in a terminal; it is not hardened for concurrent edits or large-scale deployment.

Next Steps (recommended)
------------------------

- Add stricter date parsing using `datetime.strptime` to guard against malformed dates.
- Add a simple test suite (pytest) to verify load/save/update behaviors.
- Consider adding a small SQLite backend or a web GUI if multi-user access or richer reporting is required.
