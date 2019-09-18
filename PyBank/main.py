import os
import csv


import numpy as np

HwkCSV=os.path.join(".","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

with open (HwkCSV,"r", encoding="UTF-8") as csvfile:
    readdata = csv.reader(csvfile,delimiter=",")

    csvHeader = next(readdata)

    print(f"The header is {csvHeader}")

data = []

for row in readdata:
  data.append(row)

#incase you have a header/title in the first row of your csv file, do the next line else skip it
data.pop(0) 

q1 = []  

for i in range(len(data)):
  q1.append(int(data[i][2]))

print ('Mean of 2 :            ', (np.mean(q1)))




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