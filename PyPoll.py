# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.


# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)
    # file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = (next(file_reader))

#     # Print each row in the CSV file.
#     for row in election_data:
#         # 2. Add to the total vote count.
#         total_votes += 1

# # 3. Print the total votes.
# print(total_votes)
