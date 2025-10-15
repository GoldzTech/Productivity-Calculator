def main():
    print("=== Productivity Calculator ===\n")

    try:
        num_tasks = int(input("How many tasks did you complete today? "))
    except ValueError:
        # Changed 'except' to 'except ValueError' for better practice
        print("Please enter a valid number.")
        return
    
    total_score = 0
    total_hours = 0

    for i in range(1, num_tasks + 1):
        try:
            hours = float(input(f"How many hours did you spend on task {i}? "))
            priority = int(input(f"What was the priority for task {i} (1-5)? "))
        except ValueError:
            # Changed 'except' to 'except ValueError' for better practice
            print("Please enter valid numerical values.")
            return
        
        total_hours += hours
        total_score += hours * priority

    if total_hours == 0:
        print("You did not log any hours today.")
        return
    
    productivity = total_score / total_hours
    print(f"\nYour productivity score today was: {productivity:.2f} (higher is better)")

    if productivity >= 4:
        print("Congratulations! Highly productive day!")
    elif productivity >= 2:
        print("Productive day, but there is room for improvement!")
    else:
        print("Low productivity day. Let's focus more tomorrow!")

if __name__ == "__main__":
    main()