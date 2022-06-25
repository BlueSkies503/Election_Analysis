"""Module reading election data"""
# Add our dependencies.
import csv
import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")


# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize the accumulator
total_votes = 0

# List of candidates
candidate_options = []

# Dictionary of candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""

winning_count = 0

winning_percent = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # increment vote count
        total_votes += 1
        # get name from column 3
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # add unique candidates to options list
            candidate_options.append(candidate_name)
            # begin tracking candidates votes
            candidate_votes[candidate_name] = 0

        # increment each candidates votes as they appear
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate
# by looping through the counts.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # calculate vote percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print results
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winner
    if (vote_percentage > winning_percent) and (votes > winning_count):
        winning_count = votes
        winning_percent = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percent:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
