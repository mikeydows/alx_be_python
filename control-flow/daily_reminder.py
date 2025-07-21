# Collect task details from the user
task = input("Enter your task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Initialize reminder message
reminder = ""

# Use match case for different priorities (requires Python 3.10+)
match priority:
    case "high":
        reminder = f"High Priority Reminder: {task}"
    case "medium":
        reminder = f"Medium Priority Reminder: {task}"
    case "low":
        reminder = f"Low Priority Reminder: {task}"
    case _:
        reminder = f"Reminder: {task} (Unknown priority)"

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " - that requires immediate a
