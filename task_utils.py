from datetime import datetime

# ------- VALIDATE DATE -------
def validate_date(date_str):
    """Validate date format (YYYY-MM-DD).Returns True if valid, False otherwise."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD (e.g., 2026-04-25)")
        return False

# --------- CHECK IF TASK IS OVERDUE --------
def is_overdue(task):
    """Check if a task is overdue.
    Returns True if overdue, else False."""
    try:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        today = datetime.today()

        # Check overdue condition
        if deadline < today and task["status"] != "Completed":
            return True
        return False

    except Exception:
        return False

# ----------- SHOW OVERDUE TASKS --------
def show_overdue(tasks):
    """Display all overdue tasks in the terminal."""
    today = datetime.today()
    overdue_found = False

    print("\n=================")
    print("  OVERDUE TASKS")
    print("===================")

    for index, task in enumerate(tasks, start=1):
        if is_overdue(task):
            deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
            days_overdue = (today - deadline).days

            print(f"\nTask {index}")
            print(f"Title        : {task['title']}")
            print(f"Deadline     : {task['deadline']}")
            print(f"Status       : {task['status']}")
            print(f"Days Overdue : {days_overdue} day(s)")
            print("------------------------------")

            overdue_found = True

    if not overdue_found:
        print(" No overdue tasks found!")

    print()  # spacing