import os
import csv
def Totals(election_data):
    candidate=[]
    total_number_votes=0
    winner=""
    names=[]
    output=""
    for row in csvreader:
        total_number_votes+=1
        candidate.append(row[2])
    from collections import Counter
    candidate_count= Counter(candidate)
    max_votes=max(Counter.values())
    for names,votes in candidate_count.items():
        vote_percent= round(100*votes/total_number_votes,3)
        List_candidate=f"[{names}:{vote_percent}]"
        print(f"[{names}:{vote_percent}]")    
        print (names)    
        print(vote_percent)
        print(total_number_votes)
        print (candidate_count)
    for name,votes in candidate_count.items():
        if votes==max_votes:
            winner = name
            
    Analysis = open("Analysis/Analysis.text", "w")
    Analysis.write(f"----Election Summary & Results----\n"
        f"The total number of votes cast is {total_number_votes} \n"
        f"The candidates who received votes and their corresponding total votes in this election are: {candidate_count}\n"
        f"The following are the percentages of votes that each candidate has received:{List_candidate} \n"
        f"The winner of the election based on popular vote is: {winner}\n"
        f"----------------------------------------------------------------------------------------")
    Analysis.close() 
election_data= os.path.join("Resources","election_data.csv")

with open (election_data, encoding='utf-8') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=",")
     header= next(csvreader)
     Totals(csvreader)

#complete list of candidates who received votes
#The percentage of votes each candidate won
#total number of votes each candidate won
#The winner of the election based on popular vote
