import os
import csv


import numpy as np
HwkCSV=os.path.join(".","budget_data.csv")

# Define the variables
months_total = []
net_total = []
profits = []
monthYear = []
change = 0
value = 0
net_total = 0
months_total = 0
average = 0

# Read the rows
with open(HwkCSV, "r", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    first_row = next(csvreader)
    value = int(first_row[1])

# Define the variables operation
    for row in csvreader:
        monthYear.append(row[0])
        
        net_total += int(row[1])
        months_total = months_total + 1

        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

    average = sum(profits) / len(profits)

    great_increase = max(profits)
    great_index = profits.index(great_increase)
    great_date = monthYear[great_index]

    great_decrease = min(profits)
    worst_index = profits.index(great_decrease)
    worst_date = monthYear[worst_index]

#The total number of months included in the dataset
#count.date(month)

#The net total amount of "Profit/Losses" over the entire period
#sum.profit/losses()

#The average of the changes in "Profit/Losses" over the entire period
#avg(profit/losses)

#The greatest increase in profits (date and amount) over the entire period
#max(profit/losses)

#The greatest decrease in losses (date and amount) over the entire period
#min(profit/losses)


# Print the values in the Terminal
print("Financial Analysis for PyBank")
print("-------------------------------------")
print(f"Total months: {str(months_total)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(round(average, 2))}")
print(f"Greatest increase in Profits: {str(great_date)} (${str(great_increase)})")
print(f"Greatest decrease in Profits: {str(worst_date)} (${str(great_decrease)})")

# Export the results in a text file
output = open("PyBank Output.txt", "w")

line1 = ("Financial Analysis for PyBank")
line2 = ("-------------------------------------")
line3 = str(f"Total months: {str(months_total)}")
line4 = str(f"Total: ${str(net_total)}")
line5 = str(f"Average Change: ${str(round(average, 2))}")
line6 = str(f"Greatest increase in Profits: {str(great_date)} (${str(great_increase)})")
line7 = str(f"Greatest decrease in Profits: {str(worst_date)} (${str(great_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))