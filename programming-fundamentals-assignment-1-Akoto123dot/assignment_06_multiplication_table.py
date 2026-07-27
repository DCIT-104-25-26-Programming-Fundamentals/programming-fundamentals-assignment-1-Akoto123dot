# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# -------------------------------
# PART A - Single Table
# -------------------------------

def single_table():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Error: Number must be a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")
        return

    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")


# -------------------------------
# PART B - Bonus: Tables from 1 to N
# -------------------------------

def tables_up_to_n():
    try:
        n = int(input("Enter a positive integer N: "))
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")
        return

    for num in range(1, n + 1):
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
        print("-" * 20)


# -------------------------------
# MAIN PROGRAM
# -------------------------------

def main():
    print("Multiplication Table Generator")
    print("1. Single Table")
    print("2. Tables from 1 to N")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        single_table()
    elif choice == "2":
        tables_up_to_n()
    else:
        print("Invalid choice. Please select 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()

