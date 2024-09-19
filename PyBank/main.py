# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(".","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0    #Holds the total number of months
total_net = 0       #Holds overal total
total_change = 0    #Holds total change
average_change = 0  #average change over months
GreatestInDate = "" #month of greatest increase
GreatestInTotal = 0 #greatest increase total
GreatestDeDate = "" #month of greatest decrease
GreatestDeTotal = 0 #greatest decrease total
CurrentPL = 0
PreviousMonth = 0
# Add more variables to track other necessary financial data

print(os.getcwd())
print()
print()
print(file_to_load)
print("attempting to open file")
# Open and read the csv
with open(file_to_load,'r') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    start = next(reader)
    total_net = int(start[1])
    total_months +=1
    PreviousMonth = int(start[1])
   # total_change = int(start[1])
    # Track the total and net change


    # Process each row of data
    for row in reader:

        # increment month counter
        total_months +=1
        # Track the total
        total_net += int(row[1])

        # Track the net change
        total_change += (-1*(PreviousMonth - int(row[1])))
        
        # Calculate the greatest increase in profits (month and amount)
        if ((-1*(PreviousMonth -int(row[1])))>GreatestInTotal):
            GreatestInTotal = (-1*(PreviousMonth - int(row[1])))
            GreatestInDate = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if ((-1*(PreviousMonth - int(row[1])))<GreatestDeTotal):
            GreatestDeTotal = (-1*(PreviousMonth - int(row[1])))
            GreatestDeDate = row[0]
        PreviousMonth = int(row[1])

# Calculate the average net change across the months
average_change = round(total_change/(total_months-1),2)

# Generate the output summary
#labels = ["Total Months: ","Total: ","Average Change: ","Greatest Increase in Profits: ","Greatest Decrease in Profits: "]
#data = [total_months,"${:,.2f}".format(total_net),"${:,.2f}".format(average_change), [{GreatestInDate},"${:,.2f}".format(GreatestInTotal)],[{GreatestDeDate},"${:,.2f}".format(GreatestDeTotal)]]
output = f"Financial Analysis\n\nTotalMonths: {total_months}\n\nTotal: ${total_net}\n\nAverage Change: ${average_change}\n\nGreatest Increase in Profits: {GreatestInDate} (${GreatestInTotal})\n\nGreatest Decrease in Profits: {GreatestDeDate} (${GreatestDeTotal})"
# Print the output
print("Financial Analysis")
print()
print("-"*50)
print()
print(f"Total Months: {total_months}")
print()
print(f"Total: ${total_net}")
print()
print(f"Average Change: ${average_change}")
print()
print(f"Greatest Increase in Profits: {GreatestInDate} (${GreatestInTotal}")
print()
print(f"Greatest Decrease in Profits: {GreatestDeDate} (${GreatestDeTotal})")
print()
# Write the results to a text file
with open(file_to_output, "w") as txt_file:  
 txt_file.write(output)
