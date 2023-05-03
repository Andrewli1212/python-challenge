# Dependencies
import os
import csv
# csv file path through operating system
pypoll_csv = os.path.join("Resources", "election_data.csv")
# output path to a txt file
pypoll_txt = os.path.join("analysis", "election_results.txt")

# variables, empty list, and empty dictonary
total_votes = 0
candidates = []
candidatesdict = {}
winner = ""
winner_votes = 0

# Open csv file
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    header = next(csvreader)
    # loop through the csv file and populating data into the list and dictonary
    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])

            candidatesdict[row[2]] = 0
        candidatesdict[row[2]] += 1
# Open and write in the output file
with open(pypoll_txt, "w") as txtfile:

    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes} \n"
        f"------------------------- \n"
    ) 

    print(output)
    txtfile.write(output)
    # Getting number of votes per candidate and the percentage
    for x in candidates:
        votes = candidatesdict.get(x)
        votes_percent = (float(votes)/float(total_votes))*100

        output = (
            f"{x}: {votes_percent:.3f}% ({votes}) \n"
        )

        print(output)
        txtfile.write(output)
        # condition to get the winner of the election
        if votes > winner_votes:
            winner = x
            winner_votes = votes

    output = (
        f"-------------------------\n"
        f"Winner: {winner} \n"
        f"-------------------------\n"
    )
    print(output)
    txtfile.write(output) 
