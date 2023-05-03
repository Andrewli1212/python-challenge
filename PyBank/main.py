# Dependencies
import os 
import csv

# csv file path through operating system
pybank_csv = os.path.join("Resources","budget_data.csv")

# empty lists  
total_months = []
total = []
change = []

# open csv file
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skipping the header
    header = next(csvreader)

    # for loop through the csv file to get the number of rows and sum of the profit/losses
    for row in csvreader:
        total_months.append(row[0])
        total.append(int(row[1]))

    x = sum(total)

    # loop through len(85) and getting the average change.
    for i in range(len(total)-1):
            change.append(total[i+1]-total[i])
    
    avg = round(sum(change)/len(change), 2)

    # Choosing the end month with the max/min change 
    month_increase = change.index(max(change)) + 1
    month_decrease = change.index(min(change)) + 1 

    
    # print 
    print("Financial Analysis")
    print("")
    print("----------------------------")
    print("")
    print(f"Total Months: {len(total_months)}")
    print("")
    print(f"Total: ${x}")
    print("")
    print(f"Average Change: ${avg}")
    print("")
    print(f"Greatest Increase in Profits: {total_months[month_increase]} (${(max(change))})")
    print("")
    print(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${min(change)})")

# output path to a txt file
output_file = os.path.join("Analysis","PyBank.txt")

# Open and write in the output file
with open(output_file, "w") as txt:

    output = (f"Financial Analysis \n\n"
     f"----------------------------\n\n" 
     f"Total Months: {len(total_months)}\n\n"
     f"Total: ${sum(total)} \n\n"
     f"Average Change: ${round(sum(change)/len(change), 2)}\n\n"
     f"Greatest Increase in Profits: {total_months[month_increase]} (${(max(change))})\n \n"
     f"Greatest Decrease in Profits: {total_months[month_decrease]} (${min(change)})"
     )

    txt.write(output)
     