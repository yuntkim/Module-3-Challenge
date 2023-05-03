import os
import csv

# Set variables 
dates = []
profit_or_losses = []
total = 0 
total_amount = 0
prev_profit_loss = None
now_profit_loss = 0 
profit_change = 0 
total_change = 0 
total_months = 0 
greatest_increase = 0 
greatest_decrease = 0
greatest_decrease_date = ""
greatest_increase_date = ""
average_change = 0

# Path to CSV file 
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Open the csv
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header 
    csv_header = next(csvreader)

    # Loop through csv
    for row in csvreader:
        # Store the data and profit/loss values in list 
        dates.append(row[0])
        profit_or_losses.append(float(row[1]))
        
        # Calculate total profit/loss
        total += int(row[1])
        
        # Count the total number of months
        total_months = len(dates)
        
        # Calculate the total change 
        total_amount += int(row[1])
        
        now_profit_loss = int(row[1])
        if prev_profit_loss is not None: 
            profit_change = now_profit_loss - prev_profit_loss
            total_change += profit_change
        prev_profit_loss = now_profit_loss

        # Determine the greatest increase 
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            greatest_increase_date = row[0] 

        # Determine the greatest decrease 
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_date = row[0] 

    # Calculate the average profit/loss change
    average_change = round(total_change / (total_months - 1), 2)

    # Print to the console
    result = ""
    result += "Financial Analysis\n"
    result += "---------------------------\n"
    result += f"Total Months: {total_months}\n"
    result += f"Total: ${total}\n"
    result += f"Average Change: ${float(average_change)}\n"
    result += f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    result += f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
    print(result)

    # Write to a text file
    analysis_path = os.path.join('analysis', 'analysis.txt')
    with open(analysis_path, 'w') as txtfile:
        txtfile.write("Financial Analysis\n") 
        txtfile.write("----------------------------\n")
        txtfile.write("Total Months: " + str(total_months) + "\n")
        txtfile.write("Total: $" + str(total_amount) + "\n")
        txtfile.write("Average Change: $" + str(round(average_change, 2)) + "\n")    
        txtfile.write("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")\n")
        txtfile.write("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")\n")