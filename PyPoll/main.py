import os
import csv

# Create lists and variables to store the data
ballot_ids = []
county_names = []
candidates = []
total_votes = 0 

# Path to csv file 
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Open the csv file in reading mode and set delimiter 
with open(election_data_csv, "r") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    # Loop through each row 
    for row in csvreader:     
        # Add values of each column to list
        ballot_ids.append(row[0])
        county_names.append(row[1])
        candidates.append(row[2])

# Count total number of votes
total_votes = len(ballot_ids)

# Count the number for each candidate
count_Charles = candidates.count("Charles Casper Stockham")
percentage_Charles = round(count_Charles / total_votes * 100, 3)

count_Diana = candidates.count("Diana DeGette")
percentage_Diana = round(count_Diana / total_votes * 100, 3)

count_Raymon = candidates.count("Raymon Anthony Doane")
percentage_Raymon = round(count_Raymon / total_votes * 100, 3)

# Create final counts dictionary 
final_counts = {
    "Charles Casper Stockham": count_Charles,
    "Diana DeGette": count_Diana, 
    "Raymon Anthony Doane": count_Raymon
}

# Get winner with most votes 
winner = max(final_counts, key=final_counts.get)

# Print results 
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print(f"Charles Casper Stockham: {percentage_Charles}% ({count_Charles})")
print(f"Diana DeGette: {percentage_Diana}% ({count_Diana})")
print(f"Raymon Anthony Doane: {percentage_Raymon}% ({count_Raymon})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# Path to write txt file 
analysis_path = os.path.join('analysis', 'analysis.txt')

# Write out result to txt file :) 
with open(analysis_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Charles Casper Stockham: {percentage_Charles}% ({count_Charles})\n")
    txtfile.write(f"Diana DeGette: {percentage_Diana}% ({count_Diana})\n")
    txtfile.write(f"Raymon Anthony Doane: {percentage_Raymon}% ({count_Raymon})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")