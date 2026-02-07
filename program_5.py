# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

#my code
TAX_RATE = 0.07

def calculate_total():
    # Get hot dog type
    print("Hot Dog Types:")
    print("1. Hot Dog ($3.50)")
    print("2. Chili Dog ($4.50)")
    choice = int(input("Choose a hot dog (1 or 2): "))

    if choice == 1:
        cost = 3.50
    elif choice == 2:
        cost = 4.50
    else:
        print("Invalid choice.")
        return

    # Optional toppings
    cheese = input("Add cheese for $0.50? (y/n): ")
    if cheese.lower() == 'y':
        cost += 0.50

    peppers = input("Add peppers for $0.75? (y/n): ")
    if peppers.lower() == 'y':
        cost += 0.75

    onions = input("Add grilled onions for $1.00? (y/n): ")
    if onions.lower() == 'y':
        cost += 1.00

    # Calculate tax and total
    tax = cost * TAX_RATE
    total = cost + tax

    # Display results
    print("\nHot Dog Cost: $", format(cost, ".2f"))
    print("Tax: $", format(tax, ".2f"))
    print("Total Cost: $", format(total, ".2f"))


# Run the program
calculate_total()