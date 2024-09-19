# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []         #list of candidates
votesperCandidate = []  #list of each cadidates votes
percentOfVotes = []     #list of the percentage of candidate votes
index = 0               #keep track of the index that each candidate is at
currentc = ""           #holder for the current candidate

# Winning Candidate and Winning Count Tracker
candidatewin = ""       #holder for winning candidate
winningvotes = 0        #holder for the amount of votes the winning candidate has
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        currentc = row[2]

        # If the candidate is not already in the candidate list, add them
        try: 
            index = candidates.index(currentc)
        except ValueError:
            candidates.append(currentc)
            votesperCandidate.append(0)
            percentOfVotes.append(0)
            index = len(candidates) - 1
        # Add a vote to the candidate's count
        votesperCandidate[index] +=1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    print()
    print("Election Results")
    print()
    print("-"*50)
    print()
    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")
    print()
    print("-"*50)
    print()
    # Write the total vote count to the text file
    # ["Total Votes",total_votes]
    txt_file.write(f"Election Results\nTotalVotes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for x in range(0,len(candidates)):
        # Get the vote count and calculate the percentage
        percentOfVotes[x] = round(votesperCandidate[x]/total_votes*100,3)

        # Update the winning candidate if this one has more votes
        if(votesperCandidate[x]>winningvotes):
            candidatewin=candidates[x]
            winningvotes = votesperCandidate[x]
        # Print and save each candidate's vote count and percentage
        print(f"{candidates[x]}: {percentOfVotes[x]}% ({votesperCandidate[x]})")
        print()
        txt_file.write(f"{candidates[x]}: {percentOfVotes[x]}% ({votesperCandidate[x]})\n")

    # Generate and print the winning candidate summary
    print("-"*50)
    print()
    print(f"Winner: {candidatewin}")
    print()
    print("-"*50)
    
    # Save the winning candidate summary to the text file


   # txt_file.write(zip(candidates,percentOfVotes,votesperCandidate))
    txt_file.write(f"\nWinner: {candidatewin}\n")