import os
import csv
def Totals(election_data):
    candidate=[]
    total_number_votes=0
    max_votes=661583
    winner=""
    for row in csvreader:
        total_number_votes+=1
        candidate.append(row[2])
    from collections import Counter
    candidate_count= Counter(candidate)
    for name,votes in candidate_count.items():
        vote_percent= round(100*votes/total_number_votes,3)
        print(f"{name} {vote_percent}")    
            
    print(total_number_votes)
    print (candidate_count)
    print(vote_percent)
    for name,votes in candidate_count.items():
        if votes==max_votes:
            winner = name
            max_votes = votes

   

election_data= os.path.join("Resources","election_data.csv")

with open (election_data, encoding='utf-8') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=",")
     header= next(csvreader)
     Totals(csvreader)
    
#Total number of Votes cast
#complete list of candidates who received votes
#The percentage of votes each candidate won
#total number of votes each candidate won
#The winner of the election based on popular vote
#print(f"Election Resultls"
#print(---------------------------------------------)
    # Analysis = open("Analysis/Analysis.text", "w")
    # Analysis.write(f"----Election Summary & Results----\n"
    # f"The total number of votes cast is {total_number_votes} \n"
    # f"The candidates who received votes in this election are: {}\n"
    # f"The following are the percentages of votes that each candidate has received:"{name} {vote_percent}\n"
    # f"The candidates received the following votes: {}\n"
    # f"The winner of the election based on popular vote is: {}\n"
    # f"----------------------------------------------------------------------------------------")
    # Analysis.close()