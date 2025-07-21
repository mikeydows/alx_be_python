task = input("Enter your tasks:")
priority = input("Enter your priority (high,medium,low):").lower()
time_bound = input("Is the task time bound? (yes or no):").lower()

match priority:
    case "high":
        reminder = f"Reminder: {task} {priority}"
    case "medium":
        reminder = f"Reminder: {task} {priority}"
    case "low":
        reminder = f"Reminder: {task} {priority}"
    case _:
        reminder = f"Reminder: {task} {priority}"

if time_bound =="yes":
    reminder += " - that requires immediate attention today!"
