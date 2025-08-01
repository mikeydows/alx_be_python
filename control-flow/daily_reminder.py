# daily_reminder.py

# Prompt user for task
task = input("Enter your task: ").strip()

# Loop until valid priority is entered
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Please enter a valid priority: high, medium, or low.")

# Loop until valid time-bound input is entered
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    print("Please answer with 'yes' or 'no'.")

# Match-case for priority response
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Final customized reminder with required format
if time_bound == "yes":
    print(f"Reminder: {reminder} that requires immediate attention!")
else:
    print(f"Reminder: {reminder}. It's not time-sensitive.")
