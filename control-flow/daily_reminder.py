task = input("Enter the task description: ")
priority = input("Enter the task priority (high,medium,low): ").lower()
time_bound = input("Is the task time-bound? (yes/no)").lower()

match priority:
    case "high":
        reminder = f"Reminder: {task}[Priority: HIGH]"
    case "medium":
        reminder = f"Reminder: {task}[Priority: MEDIUM]"
    case "low":
        reminder = f"Reminder: {task}[Priority: LOW]"
    case _:
        reminder = f"Reminder: f"{task}[Priority: UNKNOWN]"

if time_bound == "yes":
    reminder += "- that requires immediate attention today!"

print(reminder)
