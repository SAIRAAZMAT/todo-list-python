
def main():
    total = 0         
    count = 0          
    print("=== Expense Tracker ===")
    print("Enter expense amounts one by one.")
    print("Type 'done' or 'quit' when you are finished.\n")

    while True:  # The Logic Skeleton - continuous audit loop
        user_input = input("Enter expense amount: ").strip()

        # --- Kill Switch: Sentinel Value check ---
        if user_input.lower() in ("done", "quit", "exit"):
            break

        # --- Defensive Coding: The Gatekeeper ---
        try:
            expense = float(user_input)   

            if expense < 0:
                print("⚠ Invalid: Expense cannot be negative. Try again.\n")
                continue

        except ValueError:
            print("⚠ Invalid Data: Please enter a numeric value.\n")
            continue

        # --- The Accumulator Pattern ---
        total += expense
        count += 1
        print(f"✔ Added {expense}. Running Total: {total}\n")

    # --- Phase 3: Output ---
    print("\n=== Summary ===")
    print(f"Total Expenses Entered : {count}")
    print(f"FINAL TOTAL SPENT      : ${total:.2f}")


if __name__ == "__main__":
    main()