# The data we need to retrieve.
file_to_load = 'Resources/election_results.csv'

election_data = open(file_to_load, 'r')



import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

headers = next(file_reader)
print(headers)

    


#open(file_to_save, "w")

# 1. The total number of votes cast
# 2. A complete list of candidates with votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import datetime
now = datetime.datetime.now()
print("The time right now is ", now)

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")

