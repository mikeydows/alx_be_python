task = input("Enter your tasks:")
priority = input("Enter your priority (high,medium,low):")   
time_bound = input("Is it time bound (yes or no):")

match task:
    case priority:
        if priority=="high" | time_bound == "yes":
            print(f"Reminder:'{task}' is a {priority} priprity task that requires immediate action")
        elif priority=="medium" | time_bound == "yes":
            print(f"Reminder:'{task}' is a {priority} priority task that requires immediate action")
        elif priority=="low" | time_bound == "no":
            print(f"Reminder:'{task}' is a {priority} priority task. Consider completing it when you have free time.")