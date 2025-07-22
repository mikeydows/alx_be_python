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
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority"

# Time sensitivity
#if time_bound == "yes":
 #   reminder += " that requires immediate attention today!"
#else:
 #   reminder += ". Consider completing it when you have time."

# Final customized reminder
print("\n🔔 Reminder Details:")
print(f"Task       : {task}")
print(f"Priority   : {priority.upper()}")

if time_bound == "yes":
    print("⏱️ Action   : This task is time-sensitive — act immediately!")
else:
    print("⏳ Action   : This task is not time-sensitive — plan accordingly.")


# Final reminder
print("\n" + reminder)
