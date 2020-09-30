import os
import csv

election_data= os.path.join("Resources","election_data.csv")

with open (election_data, encoding='utf-8') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=",")
     header= next(csvreader)

#Total number of Votes cast
number of votes=0
total_number_votes+=1
print (total_number_votes)