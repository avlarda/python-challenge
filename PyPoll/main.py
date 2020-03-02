import os
import csv
import numpy as np
HwkCSV=os.path.join(".","election_data.csv")


# Define the variables
Candidates = []
votes_received = []
percent_received = []
total_votes = 0

# Read the rows
with open(HwkCSV, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

# Define the variables operation
    for row in csvreader:
        total_votes += 1

        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            votes_received.append(1)
        else:
            index = Candidates.index(row[2])
            votes_received[index] += 1
    
    for votes in votes_received:
        percentage = (votes / total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_received.append(percentage)

# The total number of votes cast
# A complete list of candidates who received votes
# # The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
    winner = max(votes_received)
    index = votes_received.index(winner)
    winner_candidate = Candidates[index]

# Print the values in the Terminal
print("Election Results")
print("------------------------")
print(f"Total votes: {str(total_votes)}")
print("------------------------")
for i in range (len(Candidates)):
    print(f"{Candidates[i]}: {str(percent_received[i])} ({str(votes_received[i])})")
print("------------------------")
print(f"Winner: {winner_candidate}")
print("------------------------")