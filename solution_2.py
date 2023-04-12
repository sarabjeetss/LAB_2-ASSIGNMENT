'''
    SARABJEET SINGH
    22049221
    SOLUTION OF QUE 2

    '''

def get_positive_float(prompt):
    """
    This function prompts the user for a positive floating-point value and returns it.
    If the value entered is not positive, it keeps tell a person until a positive value is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Enter a positive number only.")
            else:
                return value
        except ValueError:
            print("Enter the value again.")


def print_species_data(starting_count, daily_increase, num_days):
    """
    This function takes in the starting count, daily percentage increase, and number of days as inputs.
    It prints the organisms and species data for each day based on the inputs.
    """
    print(f"Day 01 count: {starting_count}")
    count = starting_count
    for day in range(2, num_days+1):
        count += count * daily_increase / 100
        print(f"Day {day:02d} count: {count:.2f}")


# Main program
starting_count = get_positive_float("Starting number of organisms and species: ")
daily_increase = get_positive_float("Average daily percentage increase: ")
num_days = int(get_positive_float("How many days' worth of data should be printed: "))

print_species_data(starting_count, daily_increase, num_days)
