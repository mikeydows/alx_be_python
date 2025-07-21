task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Note: '{task}' is a {priority} priority task"
    case "medium":
        reminder = f"Note: '{task}' is a {priority} priority task"
    case "low":
        reminder = f"Note: '{task}' is a {priority} priority task."
    case _:
        reminder = f"Reminder: {task} [Priority: UNKNOWN]"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

print(reminder)
