'''
    SARABJET SINGH
    22049221
    SOLUTION OF QUE 1

    '''
#  The variables for total and average rainfall
total_rainfall = 0
average_rainfall = 0

# Ask the user to enter the number of years
years = int(input("Enter the years: \n"))

# Loop through each year
for year in range(1, years+1):
    # Initialize the variable for the total rainfall for this year
    yearly_rainfall = 0
    
    # Loop through each month
    for month in range(1, 13):
        # Ask the user for the amount of rainfall in centimeters for this month
        rainfall_cm = float(input(f"Enter the rainfall in cm for year {year}, month {month}: "))
        
        # Add the rainfall for this month to the yearly total
        yearly_rainfall += rainfall_cm
    
    # Add the yearly total to the overall total
    total_rainfall += yearly_rainfall
    
    # Calculate and print the average monthly rainfall for this year
    average_monthly_rainfall = yearly_rainfall / 12
    print(f"Year {year} average monthly rainfall: {average_monthly_rainfall:.2f} cm")
    
# Calculate and print the average yearly rainfall over all years
average_rainfall = total_rainfall / (years * 12)
print(f"\nAverage yearly rainfall over {years} years: {average_rainfall:.2f} cm")
